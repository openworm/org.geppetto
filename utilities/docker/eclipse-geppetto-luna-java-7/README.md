# eclipse-geppetto:luna-java-7 docker file

## How to run

* Install Docker
* run ./run-bash.sh
* Within the prompt, `eclipse &` to launch eclipse

## Pre-requisites

* Docker is a CPU and hard disk hog.  Make sure you have enough of both before you start.

## What this does

* Loads an eclipse environment based on Luna with Java 7
* Installs Virgo server
* Installs Virgo tooling plugin
* Installs Ecore plugins
* Installs Base geppetto code in git repos

## What this doesn't

* Set up the workspace within eclipse
* Activate or set up the virgo server
* Install the persistence bundle.  See eclipse-geppetto:persistence for that.

## Known issues

* You need to manually import the repos via import->Maven->Existing maven project
* You need to right click and do virgo->add OSGI plan nature to model, model.swc, model.neuroml bundles
* You need to set up the virgo server yourself
* You need to pick a specific order of bundles to deploy in the server (model, core, simulation, model.swc, model.neuroml, frontend) and save the server configuration
