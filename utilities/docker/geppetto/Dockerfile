FROM java:8
MAINTAINER Stephen Larson "slarson@openworm.org"

ARG frontendBranch=development
ENV frontendBranch=${frontendBranch}
RUN echo "ECHO BRANCH ------------  $frontendBranch";

RUN apt-get update && apt-get install -qq -y sudo xvfb 

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
RUN apt-get update && apt-get install -qq -y curl bsdtar locate
USER developer
RUN mkdir -p /home/developer/virgo
RUN curl -L 'http://www.eclipse.org/downloads/download.php?file=/virgo/release/VP/3.7.2.RELEASE/virgo-tomcat-server-3.7.2.RELEASE.zip&r=1' | bsdtar --strip-components 1 -C /home/developer/virgo -xzf -
RUN chmod u+x /home/developer/virgo/bin/*.sh
ENV SERVER_HOME /home/developer/virgo
#VOLUME /home/developer/virgo
#END VIRGO INSTALL

RUN mvn --version

RUN java -version

EXPOSE 8080
CMD ["/home/developer/virgo/bin/startup.sh"]
