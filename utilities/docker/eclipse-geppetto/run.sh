./run-virgo.sh
xhost +
sudo docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v virgo:/home/developer/virgo -v workspace:/home/developer/workspace slarson/eclipse-geppetto
