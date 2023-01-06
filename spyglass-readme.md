## Setup

cd docker
./hostsetup.sh

In dandihub terminal 1
cd dshare
./deploy-mysql.sh


In dandihub terminal 2
cd dshare
./spy-d.sh

## Notes

clean.sh should cleanup the dshare dir

datajoint/mysql
- Running mysql works just fine on my local machine.
- datajoint/mysql works sometimes inside of dandihub (locally)
- I am able to use the `python3 -m huzzah.py` to connect to mysql with @root:tutoral

spyglass
- i coudlnt get the container to run, so ive just been using a python
    base image and shelling in
- on dandihub i got this to work, but ive never gotten it to work with
    mysql. together they crash my machine it seems.

Local attempt (not in dandihub)
- datajoint/mysql worked
- huzzah connected
- spyglass...
    - i have no idea what happened, but it seems like a singularity
        related "leak" into my host system. I have started hitting new
        errors like "function not imlpemented" during pip installs. This
        may be related to permissions on the host.

