# eclipse-geppetto:extsim docker file

## How to run

* Install Docker
* run ./run.sh

When you first get in, do new run as->maven installs on org.geppetto and org.geppetto.persistence.  Then do a clean on the virgo server and start it.

## Pre-requisites

* Docker is a CPU and hard disk hog.  Make sure you have at least 30GB free space and not a lot of other programs running on a decent machine before you start.

## What this does

* Loads an eclipse environment based on Luna with Java 7 with virgo tooling & ecore plugins & base geppetto code in git repos
* Installs a mysql database
* Sets up the mysql database with test data and initial guest user
* Grabs the org.geppetto.persistence code and sets it up
* Imports all the geppetto maven projects into its workspace
* Sets the Virgo Bundle nature on all code repos
* Sets up the virgo server within eclipse
* Installs NEURON with python support
* Installs the external simulator bundle in the workspace

## What this doesn't

* Fully install the bundles into the virgo server such that you can hit start and the persistence bundle works
* Loads the org.geppetto.simulator.external bundle in eclipse

## Known issues

* While the database is set up properly and running, the persistence bundle seems to have trouble talking to it until a series of run as-> maven install and virgo server resets are done.
* The version of Maven used to do builds is not the one Eclipse is using.  The maven repo directories are also different.  If these were the same, the environment may be more sane & take less disk space.
* The external simulator bundle isn't installed when eclipse starts up
