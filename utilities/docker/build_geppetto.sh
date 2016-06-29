#!/bin/bash

#Run this script with 'sudo' and run it from outside of this directory,
# at the level above the root (org.geppetto)

#If run with:
#   build_geppetto.sh clean
# it will clear out the working directories in case you get stuck in a partial state

if [[ $1 == "clean" ]]; then
    echo "Cleaning"
    docker rm my-maven-project ;
    docker stop virgo-tomcat-server
    docker rm virgo-tomcat-server
    rm -rf virgo
    rm -rf org.geppetto.*
else
    echo "Bad argument"
fi

python org.geppetto/utilities/docker/build_geppetto_docker.py
