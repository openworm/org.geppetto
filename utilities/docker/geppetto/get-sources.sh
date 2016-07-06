#!/bin/bash

mkdir -p workspace
cd workspace
python ../get-geppetto-git-repos.py
cd ..
chmod -R 777 workspace
