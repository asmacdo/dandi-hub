#
# singularity pull docker://djarecka/spyglass_tmp
# singularity build spy.simg docker://djarecka/spyglass_tmp
#
singularity build spy.simg docker://library/python
singularity run spy.simg pip3 install datajoint && pip3 install spyglass-neuro && python -m spyglass_stuff


# singularity run spy.simg pip3 install datajoint && python3 -m  spyglass_stuff
  # python -m huzzah
