#!/bin/bash

./home/developer/geppetto/check_update.sh
cd /home/developer/workspace/org.geppetto/utilities/source_setup
python update_server.py
./home/developer/virgo/bin/startup.sh
