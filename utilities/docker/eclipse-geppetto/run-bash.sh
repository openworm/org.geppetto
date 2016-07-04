xhost +
sudo docker run -ti -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix slarson/eclipse-geppetto /bin/bash
