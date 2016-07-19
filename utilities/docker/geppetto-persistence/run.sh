xhost +
sudo docker run -ti --name geppetto --publish=8080:8080 -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix slarson/geppetto:persistence
