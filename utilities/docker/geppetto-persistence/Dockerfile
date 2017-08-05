FROM java:7
MAINTAINER Stephen Larson "slarson@openworm.org"

ARG aKey
ENV aKey=${aKey}
ARG sKey
ENV sKey=${sKey}
ARG persistenceBranch
ENV persistenceBranch=${persistenceBranch}

RUN if ["$persistenceBranch" == null]; then $persistenceBranch = "development"; fi;
RUN echo "$persistenceBranch";

RUN apt-get update && apt-get install -qq -y sudo

# Install maven
RUN apt-get update

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

#VIRGO INSTALL
USER root
RUN apt-get update && apt-get install -y -qq curl bsdtar
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

COPY config.json workspace/org.geppetto/utilities/source_setup/
COPY geppetto.plan workspace/org.geppetto/

RUN cd workspace && git clone https://github.com/openworm/org.geppetto.model.git && cd org.geppetto.model && git checkout development
RUN cd workspace && git clone https://github.com/openworm/org.geppetto.core.git && cd org.geppetto.core && git checkout development
RUN cd workspace && git clone https://github.com/openworm/org.geppetto.model.neuroml.git && cd org.geppetto.model.neuroml && git checkout development
RUN cd workspace && git clone https://github.com/openworm/org.geppetto.model.swc.git && cd org.geppetto.model.swc && git checkout development
RUN cd workspace && git clone https://github.com/openworm/org.geppetto.simulation.git && cd org.geppetto.simulation && git checkout development
RUN cd workspace && git clone https://github.com/openworm/org.geppetto.frontend.git && cd org.geppetto.frontend && git checkout development
RUN cd workspace && git clone https://github.com/openworm/org.geppetto.persistence.git && cd org.geppetto.persistence && git checkout $persistenceBranch

RUN sudo chmod -R 777 workspace \
    && cd workspace/org.geppetto && mvn --quiet install
#END GET GEPPETTO SOURCES

#INSTALL MYSQL
USER root
ENV MYSQL_USER=mysql \
    MYSQL_DATA_DIR=/var/lib/mysql \
    MYSQL_RUN_DIR=/run/mysqld \
    MYSQL_LOG_DIR=/var/log/mysql

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -qq -y mysql-server \
 && rm -rf ${MYSQL_DATA_DIR} \
 && rm -rf /var/lib/apt/lists/*

RUN mkdir -p ${MYSQL_DATA_DIR} && mkdir -p ${MYSQL_RUN_DIR} && \
  mkdir -p ${MYSQL_LOG_DIR}

USER developer

#SETUP MYSQL CONFIG
RUN mkdir -p geppetto/
COPY db.properties geppetto/
COPY init.sql geppetto/
#COPY entrypoint.sh geppetto/
#RUN sudo chmod +x geppetto/entrypoint.sh
#END SETUP MYSQL CONFIG

#SETUP MYSQL INITIAL DATA
USER root
RUN mysql_install_db --user=mysql >/dev/null 2>&1
RUN sed 's/password = .*/password = /g' -i /etc/mysql/debian.cnf
RUN service mysql start && mysql -uroot < /home/developer/geppetto/init.sql
#END SETUP MYSQL INITIAL DATA

USER developer
RUN cd /home/developer/workspace/org.geppetto.persistence && mvn install --quiet && mvn install --quiet

RUN sudo service mysql start && cd /home/developer/workspace/org.geppetto.persistence && mvn exec:java -Dexec.mainClass="org.geppetto.persistence.util.DBTestData" -Dexec.classpathScope=runtime

#END INSTALL MYSQL

RUN cd /home/developer/workspace/org.geppetto/utilities/source_setup && python update_server.py

RUN sudo echo "accessKey=$aKey" > /home/developer/geppetto/aws.credentials
RUN sudo echo "secretKey=$sKey" >> /home/developer/geppetto/aws.credentials

EXPOSE 8080
CMD sudo service mysql start && /home/developer/virgo/bin/startup.sh
