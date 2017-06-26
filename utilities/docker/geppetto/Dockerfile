FROM java:7
MAINTAINER Stephen Larson "slarson@openworm.org"

RUN apt-get update && apt-get install -y sudo

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

# verify checksum
RUN echo "87e5cc81bc4ab9b83986b3e77e6b3095 /tmp/apache-maven-3.5.0-bin.tar.gz" | md5sum -c

# install maven
RUN sudo tar xzf /tmp/apache-maven-3.5.0-bin.tar.gz -C /opt/
RUN sudo ln -s /opt/apache-maven-3.5.0-bin.tar.gz /opt/maven
RUN sudo ln -s /opt/maven/bin/mvn /usr/local/bin
RUN sudo rm -f /tmp/apache-maven-3.5.0-bin.tar.gz
ENV MAVEN_HOME /opt/maven
RUN mvn --version

#VIRGO INSTALL
USER root
RUN apt-get update && apt-get install -y curl bsdtar maven
USER developer
RUN mkdir -p /home/developer/virgo
RUN curl -L 'http://www.eclipse.org/downloads/download.php?file=/virgo/release/VP/3.6.4.RELEASE/virgo-tomcat-server-3.6.4.RELEASE.zip&mirror_id=580&r=1' | bsdtar --strip-components 1 -C /home/developer/virgo -xzf -
RUN chmod u+x /home/developer/virgo/bin/*.sh
ENV SERVER_HOME /home/developer/virgo
#VOLUME /home/developer/virgo
#END VIRGO INSTALL

#GET GEPPETTO SOURCES
USER root
RUN mkdir -p workspace && cd workspace && git clone http://github.com/openworm/org.geppetto && cd org.geppetto && git checkout development
RUN chmod -R 777 workspace
USER developer
RUN cd workspace/org.geppetto/utilities/source_setup && yes n | python setup.py && python gitall.py pull \
    && python gitall.py reset && python gitall.py checkout development && cd ../../../.. && sudo chmod -R 777 workspace \
    && cd workspace/org.geppetto && mvn install
#END GET GEPPETTO SOURCES

RUN mkdir -p geppetto/

#COPY entrypoint.sh geppetto/
#COPY check_update.sh geppetto/
#RUN sudo chmod +x geppetto/*.sh

RUN cd /home/developer/workspace/org.geppetto/utilities/source_setup && python update_server.py

CMD /home/developer/virgo/bin/startup.sh