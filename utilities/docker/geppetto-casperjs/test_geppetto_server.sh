#!/bin/sh
while ! curl http://192.168.99.100:8080/org.geppetto.frontend
do
  echo "$(date) - still trying"
  sleep 1
done
echo "$(date) - connected successfully"
