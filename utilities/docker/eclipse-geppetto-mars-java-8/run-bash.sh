xhost +
#./run-virgo.sh
#sudo docker run -ti -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix  -v virgo:/home/developer/virgo -v workspace:/home/developer/workspace slarson/eclipse-geppetto /bin/bash
#sudo docker run -ti -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --volumes-from virgo-server -v $PWD/workspace:/home/developer/workspace slarson/eclipse-geppetto /bin/bash
sudo docker run -ti --publish=8080:8080 -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --volumes-from virgo-server -v $PWD/workspace:/home/developer/workspace -v $PWD/.m2:/home/developer/.m2 slarson/eclipse-geppetto /bin/bash
