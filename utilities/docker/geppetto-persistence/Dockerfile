FROM slarson/geppetto:latest
MAINTAINER Stephen Larson "slarson@openworm.org"

USER developer

#GET GEPPETTO PERSISTENCE SOURCES
COPY config.json workspace/org.geppetto/utilities/source_setup/
COPY geppetto.plan workspace/org.geppetto/

RUN cd workspace/org.geppetto/utilities/source_setup && python setup.py
RUN sudo chmod -R 777 workspace

RUN cd workspace/org.geppetto.persistence && mvn install

#END GET GEPPETTO PERSISTENCE SOURCES

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

#END INSTALL MYSQL

USER developer

#SETUP MYSQL CONFIG
RUN mkdir -p geppetto/
COPY db.properties geppetto/
COPY init.sql geppetto/
COPY entrypoint.sh geppetto/
RUN sudo chmod +x geppetto/entrypoint.sh
#END SETUP MYSQL CONFIG

CMD /home/developer/geppetto/entrypoint.sh
