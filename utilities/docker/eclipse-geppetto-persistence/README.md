# eclipse-geppetto:persistence docker file

## How to run

* Install Docker
* run ./run-bash.sh
* Within the prompt, `eclipse &` to launch eclipse

## Pre-requisites

* Docker is a CPU and hard disk hog.  Make sure you have enough of both before you start.

## What this does

* Loads an eclipse environment based on Luna with Java 7 with virgo tooling & ecore plugins & base geppetto code in git repos
* Installs a mysql database
* Sets up the mysql database with test data and initial guest user
* Grabs the org.geppetto.persistence code and sets it up
* Imports all the geppetto maven projects into its workspace
* Sets the Virgo Bundle nature on all code repos
* Sets up the virgo server within eclipse

## What this doesn't

* Fully install the bundles into the virgo server such that you can hit start and the persistence bundle works

## Known issues

* While the database is set up properly and running, the persistence bundle seems to have trouble talking to it until a series of run as-> maven install and virgo server resets are done.
