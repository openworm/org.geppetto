#!/bin/bash

./get-sources.sh
../virgo-tomcat-server-3.6.4-RELEASE-jre-7/build.sh
../virgo-tomcat-server-3.6.4-RELEASE-jre-7/run-without-port-expose.sh
cd ../eclipse-geppetto-luna-java-7
./rebuild.sh
./run-bash.sh

#Inside the docker container, run the update_server.py before launching eclipse
