# `extraConfig` in hub config is evaluated at the end of jupyterhub_config.py
import json
import os  # noqa
import warnings  # noqa

from kubernetes_asyncio import client
from oauthenticator.github import GitHubOAuthenticator
from tornado.httpclient import AsyncHTTPClient, HTTPClientError, HTTPRequest


def modify_pod_hook(spawner, pod):  # noqa
    pod.spec.containers[0].security_context = client.V1SecurityContext(privileged=True)
    return pod


# define our OAuthenticator with `.pre_spawn_start`
# for passing auth_state into the user environment
# Based on <https://github.com/jupyterhub/oauthenticator/blob/master/examples/auth_state/jupyterhub_config.py>:  # noqa
class IsDandiUserAuthenticator(GitHubOAuthenticator):
    async def check_allowed(self, username, auth_model):
        """
        Query DANDI API to ensure user is registered.
        """
        if auth_model["auth_state"].get("scope", []):
            scopes = []
            for val in auth_model["auth_state"]["scope"]:
                scopes.extend(val.split(","))
            auth_model["auth_state"]["scope"] = scopes
        auth_model = await self.update_auth_model(auth_model)

        # Allowed if admin
        if await super().check_allowed(username, auth_model):
            return True

        # Allowed if user is a registered DANDI user.
        req = HTTPRequest(
            f"${dandi_api_domain}/api/users/search/?username={username}",  # noqa
            method="GET",
            headers={
                "Accept": "application/json",
                "User-Agent": "JupyterHub",
                "Authorization": "token ${danditoken}",
            },
            validate_cert=self.validate_server_cert,
        )
        try:
            client = AsyncHTTPClient()
            print(f"Attempting to validate {username} with ${dandi_api_domain}")  # noqa
            resp = await client.fetch(req)
        except HTTPClientError as e:
            print(
                f"Dandi API request to validate {username} returned HTTPClientError: {e}"
            )
            return False
        else:
            if resp.body:
                resp_json = json.loads(resp.body.decode("utf8", "replace"))
                for val in resp_json:
                    if val["username"].lower() == username.lower():
                        return True

        # If not explicitly allowed, not allowed.
        return False

    async def pre_spawn_start(self, user, spawner):
        auth_state = await user.get_auth_state()
        if not auth_state:
            # user has no auth state
            return
        # define some environment variables from auth_state
        spawner.environment["GITHUB_TOKEN"] = auth_state["access_token"]
        spawner.environment["GITHUB_USER"] = auth_state["github_user"]["login"]
        spawner.environment["GITHUB_EMAIL"] = auth_state["github_user"]["email"]


c.KubeSpawner.modify_pod_hook = modify_pod_hook  # noqa
if "${auth_type}" == "dandi_api":
    c.JupyterHub.authenticator_class = IsDandiUserAuthenticator  # noqa
elif "${auth_type}" == "github":
    c.JupyterHub.authenticator_class = GitHubOAuthenticator  # noqa

c.GitHubOAuthenticator.enable_auth_state = True  # noqa
