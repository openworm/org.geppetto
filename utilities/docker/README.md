Geppetto Dockerfiles & Scripts
==============================

Files and directories here help to build [Docker](http://docker.com) files to load up Geppetto easily.

## Early attempt at setting Geppetto up via docker.

Should work but currently not the recommended approach.

* build_geppetto.sh             
* build_geppetto_docker.py      

## Sets up the version of Virgo that is setup for Geppetto, to be run as a separate service.

This was part of an approach to run virgo completely self contained, but had issues on the target setup of 
introducing a big performance hit.

* virgo-tomcat-server-3.6.4-RELEASE-jre-7

## Server-only geppetto

These directories install geppetto as a server only, ready to go at port 8080.  The directory with 'persistence' adds a 
pre-installed mysql and the org.geppetto.persistence module.

* geppetto
* geppetto-persistence

## Geppetto within Eclipse

The following directories contain a Dockerfile and supporting scripts to run vanilla Geppetto (the six main modules) out of the 
box WITHIN Eclipse.

Currently only luna-java-7 is known to work 100%, whereas mars-java-8 is still a work in progress.

* eclipse-geppetto-luna-java-7  
* eclipse-geppetto-mars-java-8  

## Advanced Geppetto within Eclipse

The persistence directory builds on luna-java-7 and adds the org.geppetto.persistence bundle, along with a pre-installed mysql.

The persistence directory has a few advantages over the luna-java-7 Dockerfile in that it adds eclipse workspace information so it 
starts up without requiring the developer to import the directories manually

* eclipse-geppetto-persistence        

The extsim directory builds on the persistence build and adds the org.geppetto.simulator.external module, along with installing NEURON.

* eclipse-geppetto-persist-extsim  



