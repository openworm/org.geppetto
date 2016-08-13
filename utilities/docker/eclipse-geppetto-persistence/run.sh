xhost +
sudo docker run -d --publish=8080:8080 -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --name eclipse-geppetto slarson/eclipse-geppetto:persistence
