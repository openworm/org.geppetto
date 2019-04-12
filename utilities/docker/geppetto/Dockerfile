FROM java:8
MAINTAINER Stephen Larson "slarson@openworm.org"

ARG mainBranch=development
ENV mainBranch=${mainBranch}
RUN echo "USE GIT BRANCH ------------  $mainBranch";

USER root

COPY sources.list /etc/apt/sources.list
RUN rm /etc/apt/sources.list.d/jessie-backports.list

RUN apt-get -o Acquire::Check-Valid-Until=false update && apt-get install -qq -y sudo xvfb  

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

# get maven 3.5.2
RUN sudo wget -q --no-verbose -O /tmp/apache-maven-3.5.2-bin.tar.gz http://archive.apache.org/dist/maven/maven-3/3.5.2/binaries/apache-maven-3.5.2-bin.tar.gz

# install maven
RUN sudo tar xzf /tmp/apache-maven-3.5.2-bin.tar.gz -C /opt/
RUN sudo ln -s /opt/apache-maven-3.5.2 /opt/maven
RUN sudo ln -s /opt/maven/bin/mvn /usr/local/bin
RUN sudo rm -f /tmp/apache-maven-3.5.2-bin.tar.gz
ENV MAVEN_HOME /opt/maven
RUN mvn --version

#VIRGO INSTALL
USER root
RUN apt-get -o Acquire::Check-Valid-Until=false update && apt-get install -qq -y curl bsdtar locate
USER developer
RUN mkdir -p /home/developer/virgo
RUN curl -L 'http://www.eclipse.org/downloads/download.php?file=/virgo/release/VP/3.7.2.RELEASE/virgo-tomcat-server-3.7.2.RELEASE.zip&r=1' | bsdtar --strip-components 1 -C /home/developer/virgo -xzf -
ADD dmk.sh /home/developer/virgo/bin/
RUN rm /home/developer/virgo/configuration/java-server.profile
ADD java-server.profile /home/developer/virgo/configuration/
RUN rm /home/developer/virgo/configuration/tomcat-server.xml
ADD tomcat-server.xml /home/developer/virgo/configuration/
USER root
RUN chown developer /home/developer/virgo/bin/dmk.sh
USER developer
RUN chmod u+x /home/developer/virgo/bin/*.sh
ENV SERVER_HOME /home/developer/virgo
#VOLUME /home/developer/virgo
#END VIRGO INSTALL

RUN mvn --version

#GET GEPPETTO SOURCES
USER root
RUN mkdir -p workspace && cd workspace && git clone -b development http://github.com/openworm/org.geppetto && cd org.geppetto && git checkout development
RUN chmod -R 777 workspace
USER developer

RUN cd workspace && git clone https://github.com/openworm/org.geppetto.model.git && cd org.geppetto.model && git checkout $mainBranch
RUN cd workspace && git clone https://github.com/openworm/org.geppetto.core.git && cd org.geppetto.core && git checkout $mainBranch
RUN cd workspace && git clone https://github.com/openworm/org.geppetto.model.neuroml.git && cd org.geppetto.model.neuroml && git checkout $mainBranch
RUN cd workspace && git clone https://github.com/openworm/org.geppetto.simulation.git && cd org.geppetto.simulation && git checkout $mainBranch
RUN cd workspace && git clone https://github.com/openworm/org.geppetto.frontend.git && cd org.geppetto.frontend && git checkout $mainBranch
RUN sudo chmod -R 777 workspace \
    && cd workspace/org.geppetto && mvn -Dhttps.protocols=TLSv1.2 --quiet install 
#END GET GEPPETTO SOURCES

RUN mkdir -p geppetto/
RUN mkdir rm /home/developer/virgo/./repository/usr

#COPY entrypoint.sh geppetto/
#COPY check_update.sh geppetto/
#RUN sudo chmod +x geppetto/*.sh

RUN cd /home/developer/workspace/org.geppetto/utilities/source_setup && python update_server.py

RUN java -version

EXPOSE 8080
CMD ["/home/developer/virgo/bin/startup.sh"]
