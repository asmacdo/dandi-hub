# singularity pull docker://djarecka/spyglass_tmp
# singularity pull docker://library/mysql
singularity pull docker://datajoint/mysql:5.7
# singularity build spy.simg docker://library/python
# pip install singularity-compose


# WARNING running this one with these scripts killed my machine :)
singularity build mysql.simg docker://datajoint/mysql:5.7


