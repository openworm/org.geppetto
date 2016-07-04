xhost +
./run-virgo.sh
sudo docker run -ti -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix  -v virgo:/home/developer/virgo -v workspace:/home/developer/workspace slarson/eclipse-geppetto /bin/bash
