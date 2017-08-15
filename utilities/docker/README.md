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

## Building and Running Dockerfiles
To build the geppetto and geppetto-persistence Dockerfiles use:

For geppetto
* docker build -t="geppetto" --build-arg frontendBranch=development https://github.com/openworm/org.geppetto.git#development:utilities/docker/geppetto/

and for geppetto-persistence

* docker build -t="geppetto_persistence" --build-arg frontendBranch=development --build-arg persistenceBranch=development --build-arg aKey=$accessKey --build-arg sKey=$secretKey https://github.com/openworm/org.geppetto.git#development:utilities/docker/geppetto-persistence/

The geppetto dockerfile takes in an argument as part of the build, this argument is called frontendBranch. 
With it you can specify the branch that will be used for the bundle org.geppetto.frontend when the dockerfile
starts to build.

For the geppetto-persistence it also takes an argument, persistenceBranch, which specifies the org.geppetto.persistence branch to use as part of the dockerfile build. 
It is also necessary to pass the aws.credentials of the Amazon where the projects will get persisted.
To pass the aws.credentials use build arguments aKey and sKey, for accessKey and secreteKey respectively.

Once they are done building successfully, use the following command to run them.

For Geppetto:
* docker run  -t -dit --name=geppetto_container -h localhost -p  28081:8080 geppetto

and for geppetto-persistence:
* docker run  -t -dit --name=geppetto_persistence_container -h localhost -p 28081:8080 geppetto_persistence;

The --name argument is not necessary, but makes it easier to identify the running docker containers if each docker
run is given a unique name. 

The arguments "-h localhost -p 28081:8080" specify the host address and port where the docker container wiill be run. 
This means in the command samples above, to launch geppetto you'll do it with URL "localhost:28081/org.geppetto.frontend"


