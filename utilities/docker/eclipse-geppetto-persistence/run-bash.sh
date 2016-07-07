xhost +
sudo docker run --name geppetto-mysql -e MYSQL_ROOT_PASSWORD=geppetto -d mysql:latest
sudo docker cp init.sql geppetto-mysql:/
sudo docker exec geppetto-mysql sh -c "mysql -uroot -p'geppetto' < init.sql"
sudo docker run -ti --publish=8080:8080 -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --link geppetto-mysql:mysql slarson/eclipse-geppetto:persistence sh -c 'cd workspace/org.geppetto.persistence; mvn exec:java -Dexec.mainClass="org.geppetto.persistence.util.DBTestData" -Dexec.classpathScope=runtime; /bin/bash'
