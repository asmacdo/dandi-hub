# singularity pull docker://djarecka/spyglass_tmp
# singularity pull docker://_/mysql
pip install singularity-compose


# WARNING running this one with these scripts killed my machine :)
# singularity build mysql.simg docker://datajoint/mysql

singularity build mysql.simg docker://library/mysql
singularity build python.simg docker://library/python
export MYSQL_ALLOW_EMPTY_PASSWORD=yes
singularity run \
  -B /home/jovyan/dshare/mysql:/var/lib/mysql \
  -B /home/jovyan/dshare/tmp/:/var/tmp/ \
  -B /home/jovyan/dshare/run/:/var/run/mysqld/ \
  --env MYSQL_ALLOW_EMPTY_PASSWORD=yes\
  mysql.simg
# singularity-compose up


# singularity -vvv run mysql_latest  /bin/bash
# singularity shell mysql.simg

# singularity run  --fakeroot mysql_latest.sif bash
