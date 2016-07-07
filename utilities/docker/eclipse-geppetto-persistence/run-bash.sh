xhost +
#./run-virgo.sh
#sudo docker run -ti -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix  -v virgo:/home/developer/virgo -v workspace:/home/developer/workspace slarson/eclipse-geppetto /bin/bash
#sudo docker run -ti -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --volumes-from virgo-server -v $PWD/workspace:/home/developer/workspace slarson/eclipse-geppetto /bin/bash
mkdir -p .m2
chmod 777 .m2
sudo docker run --name geppetto-mysql -e MYSQL_ROOT_PASSWORD=geppetto -d mysql:latest
#mysql -h hostname -u user database < path/to/test.sql
sudo docker run -it --link geppetto-mysql:mysql --rm mysql sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD" -e "dropcreate database geppetto;flush privileges;create user user_name identified by password;grant all privileges on geppetto.* to user_name@localhost identified by password;"'
sudo docker run -ti --publish=8080:8080 -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $PWD/.m2:/home/developer/.m2 --link geppetto-mysql:mysql slarson/eclipse-geppetto:persistence /bin/bash
