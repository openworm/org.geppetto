#!/bin/bash
if [ -n "$1" ]; then
sudo docker run -d --name geppetto --publish=8080:8080 -e BRANCH=$1 slarson/geppetto:latest
else
sudo docker run -d --name geppetto --publish=8080:8080 slarson/geppetto:latest
fi
