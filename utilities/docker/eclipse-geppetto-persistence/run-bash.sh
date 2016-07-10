xhost +
sudo docker run -ti --publish=8080:8080 -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix slarson/eclipse-geppetto:persistence sh -c 'geppetto/entrypoint.sh &; /bin/bash'
