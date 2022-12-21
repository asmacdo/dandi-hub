docker build -f Dockerfile -t hubby

docker run -it --rm --privileged -p 8888:8888 -v $PWD/dshare/:/home/jovyan/dshare/ hubby
