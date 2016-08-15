FROM slarson/eclipse-geppetto:luna-java-7

MAINTAINER stephen@openworm.org

USER developer
RUN cd ~/workspace/ && git clone http://github.com/openworm/org.geppetto.persistence \
  && cd org.geppetto.persistence && mvn install

ADD config.json workspace/org.geppetto/utilities/source_setup/

RUN mkdir -p geppetto/
ADD db.properties geppetto/

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

ADD init.sql geppetto/

RUN mkdir -p ${MYSQL_DATA_DIR} && mkdir -p ${MYSQL_RUN_DIR} && \
  mkdir -p ${MYSQL_LOG_DIR}

USER developer

#END INSTALL MYSQL

ADD entrypoint.sh geppetto/
RUN sudo chmod +x geppetto/entrypoint.sh

COPY workspace.tar.gz /home/developer/workspace
RUN cd workspace && tar -xvzf workspace.tar.gz

CMD /home/developer/geppetto/entrypoint.sh
