FROM java:7
MAINTAINER Stephen Larson "slarson@openworm.org"

RUN apt-get update && apt-get install -y sudo xvfb

RUN useradd -ms /bin/bash developer

RUN mkdir -p /home/developer && mkdir -p /etc/sudoers.d \
    echo "developer:x:1000:1000:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:1000:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown developer:developer -R /home/developer && \
    chown root:root /usr/bin/sudo && chmod 4755 /usr/bin/sudo

USER developer
ENV HOME /home/developer
WORKDIR /home/developer

# get maven 3.5.0
RUN sudo wget --no-verbose -O /tmp/apache-maven-3.5.0-bin.tar.gz http://archive.apache.org/dist/maven/maven-3/3.5.0/binaries/apache-maven-3.5.0-bin.tar.gz

# install maven
RUN sudo tar xzf /tmp/apache-maven-3.5.0-bin.tar.gz -C /opt/
RUN sudo ln -s /opt/apache-maven-3.5.0 /opt/maven
RUN sudo ln -s /opt/maven/bin/mvn /usr/local/bin
RUN sudo rm -f /tmp/apache-maven-3.5.0-bin.tar.gz
ENV MAVEN_HOME /opt/maven
RUN mvn --version

#VIRGO INSTALL
USER root
RUN apt-get update && apt-get install -y curl bsdtar locate
USER developer
RUN mkdir -p /home/developer/virgo
RUN curl -L 'http://www.eclipse.org/downloads/download.php?file=/virgo/release/VP/3.6.4.RELEASE/virgo-tomcat-server-3.6.4.RELEASE.zip&mirror_id=580&r=1' | bsdtar --strip-components 1 -C /home/developer/virgo -xzf -
RUN chmod u+x /home/developer/virgo/bin/*.sh
ENV SERVER_HOME /home/developer/virgo
#VOLUME /home/developer/virgo
#END VIRGO INSTALL

RUN mvn --version

#GET GEPPETTO SOURCES
USER root
RUN mkdir -p workspace && cd workspace && git clone http://github.com/openworm/org.geppetto && cd org.geppetto && git checkout development
RUN chmod -R 777 workspace
USER developer
RUN cd workspace/org.geppetto/utilities/source_setup && yes n | python setup.py && python gitall.py pull \
    && python gitall.py reset && python gitall.py checkout development && cd ../../../.. && sudo chmod -R 777 workspace \
    && cd workspace/org.geppetto && mvn  install 
#END GET GEPPETTO SOURCES

RUN mkdir -p geppetto/

#COPY entrypoint.sh geppetto/
#COPY check_update.sh geppetto/
#RUN sudo chmod +x geppetto/*.sh

RUN cd /home/developer/workspace/org.geppetto/utilities/source_setup && python update_server.py

CMD /home/developer/virgo/bin/startup.sh

# install node and npm plus update firefox
RUN sudo apt-get install -y nodejs npm
RUN sudo apt-get install -y nodejs-legacy
RUN sudo apt-get install -y xvfb libxrender-dev libasound2 libdbus-glib-1-2 libgtk2.0-0 bzip2
RUN cd /usr/local && sudo wget --no-verbose -O /tmp/firefox-50.0.tar.bz2 http://ftp.mozilla.org/pub/firefox/releases/50.0/linux-x86_64/en-US/firefox-50.0.tar.bz2
RUN sudo tar xvjf /tmp/firefox-50.0.tar.bz2
RUN cd ~ && sudo ln -s firefox-50.0.tar.bz2

# install casperjs needed libraries
RUN sudo npm install --silent -g phantomjs
RUN sudo npm install --silent -g casperjs

# set up dir for running caspers tests
RUN sudo curl -k -O https://download.slimerjs.org/releases/0.10.3/slimerjs-0.10.3.tar.bz2
RUN sudo pwd && tar -xjpvf slimerjs-0.10.3.tar.bz2
RUN sudo rm slimerjs-0.10.3.tar.bz2
WORKDIR /home/developer/workspace/org.geppetto.frontend/src/main/webapp/js/pages/tests/casperjs
RUN casperjs --version
RUN sudo apt-get install -y libgtk-3-dev
ENV SLIMERJSLAUNCHER  /home/developer/firefox/firefox
ENV SLIMERJS_EXECUTABLE /home/developer/slimerjs-0.10.3/slimerjs
RUN xvfb-run -a  casperjs test --includes=CoreTestsUtility.js CoreTests.js --engine=slimerjs