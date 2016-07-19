FROM java:7
MAINTAINER Stephen Larson "slarson@openworm.org"

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
COPY get-sources.sh /home/developer
COPY get-geppetto-git-repos.py /home/developer
USER root
RUN chmod +x get-sources.sh
USER developer
RUN ./get-sources.sh
RUN cd workspace/org.geppetto && mvn install
#VOLUME /home/developer/workspace
#END GET GEPPETTO SOURCES

RUN cd workspace/ && git clone http://github.com/openworm/org.geppetto.persistence \
  && cd org.geppetto.persistence && mvn install

COPY config.json workspace/org.geppetto/utilities/source_setup/
RUN cd workspace/org.geppetto/utilities/source_setup && python update_server.py

RUN mkdir -p geppetto/
COPY db.properties geppetto/

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

COPY init.sql geppetto/

RUN mkdir -p ${MYSQL_DATA_DIR} && mkdir -p ${MYSQL_RUN_DIR} && \
  mkdir -p ${MYSQL_LOG_DIR}

#END INSTALL MYSQL

USER developer

COPY entrypoint.sh geppetto/
RUN sudo chmod +x geppetto/entrypoint.sh

CMD /home/developer/geppetto/entrypoint.sh
