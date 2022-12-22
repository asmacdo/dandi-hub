# singularity pull docker://djarecka/spyglass_tmp
# singularity pull docker://library/mysql
# pip install singularity-compose


# WARNING running this one with these scripts killed my machine :)
# singularity build mysql.simg docker pull datajoint/mysql:8.0.18

# singularity build mysql.simg docker://library/mysql
# singularity build python.simg docker://library/python
# export MYSQL_ALLOW_EMPTY_PASSWORD=yes
export SINGULARITYENV_MYSQL_ALLOW_EMPTY_PASSWORD=yes
export SINGULARITYENV_MYSQL_USER=jovyan
export SINGULARITYENV_MYSQL_PASSWORD=asdf

singularity run -B /home/jovyan/dshare/mysql/:/var/lib/mysql/ -B /home/jovyan/dshare/run/:/var/run/mysqld/ mysql.simg
  # -B /home/jovian/dshare/usharemysql/:/usr/share/mysql/ \
  # -B /home/jovyan/dshare/tmp/:/var/tmp/ \

# singularity-compose up


# singularity -vvv run mysql_latest  /bin/bash
# singularity shell mysql.simg
# singularity run  --fakeroot mysql_latest.sif bash
