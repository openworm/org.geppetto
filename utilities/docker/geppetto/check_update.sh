#!/bin/bash
cd /home/developer/workspace/org.geppetto/utilities/source_setup
#if the environment variable is set, check out the latest in that branch and use it
if [ -n "$BRANCH" ]; then
git pull
git reset --hard
git checkout dockerfile
python gitall.py pull
python gitall.py reset
python gitall.py checkout development
python gitall.py checkout $BRANCH
cd /home/developer/workspace/org.geppetto/
git checkout development
mvn install
else
cd /home/developer/workspace/org.geppetto/
mvn install
fi
