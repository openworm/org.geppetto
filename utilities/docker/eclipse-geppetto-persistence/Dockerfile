FROM slarson/eclipse-geppetto:luna-java-7

MAINTAINER stephen@openworm.org

USER developer
RUN cd workspace/ && git clone http://github.com/openworm/org.geppetto.persistence \
  && cd org.geppetto.persistence && mvn install

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

USER developer
#END INSTALL MYSQL

ADD init.sql geppetto/
ADD db-entrypoint.sh geppetto/

CMD /usr/local/bin/eclipse
