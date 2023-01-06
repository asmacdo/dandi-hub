#
# singularity pull docker://djarecka/spyglass_tmp
# singularity build spy.simg docker://djarecka/spyglass_tmp
#
singularity build spy.simg docker://library/python


# singularity run spy.simg pip3 install datajoint && python3 -m  spyglass_stuff
singularity shell spy.simg 
# POC
# pip3 install datajoint spyglass-neuro mysql-connector-python
# python -m huzzah

# spyglass
# pip3 install datajoint spyglass-neuro 
# python -m spyglass_stuff
