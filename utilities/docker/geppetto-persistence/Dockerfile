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
RUN mkdir -p workspace && cd workspace && git clone http://github.com/openworm/org.geppetto
RUN chmod -R 777 workspace
USER developer

COPY config.json workspace/org.geppetto/utilities/source_setup/
COPY geppetto.plan workspace/org.geppetto/

RUN cd workspace/org.geppetto/utilities/source_setup && python setup.py && python gitall.py pull && python gitall.py reset && python gitall.py checkout development
RUN sudo chmod -R 777 workspace

RUN cd workspace/org.geppetto && mvn install
#END GET GEPPETTO SOURCES

#INSTALL MYSQL
USER root
ENV MYSQL_USER=mysql \
    MYSQL_DATA_DIR=/var/lib/mysql \
    MYSQL_RUN_DIR=/run/mysqld \
    MYSQL_LOG_DIR=/var/log/mysql

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server \
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
RUN cd /home/developer/workspace/org.geppetto.persistence && mvn install && mvn install

RUN sudo service mysql start && cd /home/developer/workspace/org.geppetto.persistence && mvn exec:java -Dexec.mainClass="org.geppetto.persistence.util.DBTestData" -Dexec.classpathScope=runtime


#END INSTALL MYSQL

RUN cd /home/developer/workspace/org.geppetto/utilities/source_setup && python update_server.py

CMD sudo service mysql start && /home/developer/virgo/bin/startup.sh
