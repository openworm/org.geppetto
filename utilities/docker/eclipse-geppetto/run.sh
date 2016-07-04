xhost +
sudo docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v virgo:/virgo slarson/eclipse-geppetto
