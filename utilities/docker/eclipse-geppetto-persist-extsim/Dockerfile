FROM slarson/eclipse-geppetto:persistence

MAINTAINER stephen@openworm.org

USER developer
RUN cd ~/workspace/ && git clone http://github.com/openworm/org.geppetto.simulator.external 

#INSTALL NEURON

RUN wget http://www.neuron.yale.edu/ftp/neuron/versions/v7.3/nrn-7.3.tar.gz && tar xzvf nrn-7.3.tar.gz
RUN sudo apt-get update && sudo apt-get install -y g++ python-dev ncurses-dev make
RUN cd nrn-7.3 && ./configure --prefix `pwd` --without-iv --with-nrnpython && make && make install
RUN cd nrn-7.3/src/nrnpython && sudo python setup.py install

#END INSTALL NEURON

ENV NEURON_HOME /home/developer/nrn-7.3/x86_64/bin/
COPY app-config.xml /home/developer/workspace/org.geppetto.simulator.external/src/main/java/META-INF/spring/
RUN sudo chmod +x /home/developer/nrn-7.3/bin/*
RUN cd workspace/org.geppetto.simulator.external && mvn install
ADD config.json workspace/org.geppetto/utilities/source_setup/
RUN cd ~/workspace/org.geppetto/utilities/source_setup && python update_server.py eclipse
