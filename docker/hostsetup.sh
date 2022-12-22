source ./clean.sh
docker build -f Dockerfile . -t hubby

docker run --privileged -it --rm -p 8888:8888 -v $PWD/dshare/:/home/jovyan/dshare/ hubby
