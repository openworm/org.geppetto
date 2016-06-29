#!/bin/bash

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
