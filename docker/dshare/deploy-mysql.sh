# singularity build mysql.simg docker://library/mysql
# singularity build python.simg docker://library/python
# export MYSQL_ALLOW_EMPTY_PASSWORD=yes
# export APPTAINERENV_MYSQL_ALLOW_EMPTY_PASSWORD=yes
# export APPTAINERENV_MYSQL_USER=jovyan
export APPTAINERENV_MYSQL_PASSWORD=tutorial
# export SINGULARITYENV_MYSQL_ALLOW_EMPTY_PASSWORD=yes
#.
# export SINGULARITYENV_MYSQL_USER=jovyan
# export SINGULARITYENV_MYSQL_PASSWORD=asdf
export APPTAINERENV_MYSQL_ROOT_PASSWORD=tutorial
singularity run -B /home/jovyan/dshare/mysql/:/var/lib/mysql/ -B /home/jovyan/dshare/run/:/var/run/mysqld/ -B /home/jovyan/dshare/config/:/etc/mysql/ -B /home/jovyan/dshare/mysql-files/:/var/lib/mysql-files/ mysql.simg
  # -B /home/jovian/dshare/usharemysql/:/usr/share/mysql/ \
  # -B /home/jovyan/dshare/tmp/:/var/tmp/ \

# singularity-compose up


# singularity -vvv run mysql_latest  /bin/bash
# singularity shell mysql.simg
# singularity run  --fakeroot mysql_latest.sif bash
