FROM metacell/java-virgo-maven:development
LABEL maintainer="Facundo Rodriguez <facundo@metacell.us>"

ARG aKey
ENV aKey=${aKey}
ARG sKey
ENV sKey=${sKey}

ARG targetBranch=master
ARG originBranch=master
ARG defaultBranch=master
RUN /bin/echo -e "\e[1;35mORIGIN BRANCH ------------ $originBranch\e[0m" &&\
  /bin/echo -e "\e[1;35mTARGET BRANCH ------------ $targetBranch\e[0m" &&\
  /bin/echo -e "\e[1;35mDEFAULT BRANCH ------------ $defaultBranch\e[0m"

# get geppetto
RUN mkdir -p workspace &&\
  cd workspace &&\
  ../copy.sh http://github.com/openworm/org.geppetto.git "${targetBranch}" "${originBranch}" "${defaultBranch}"

COPY config.json workspace/org.geppetto/utilities/source_setup/
RUN sudo mv /home/developer/workspace/org.geppetto/utilities/docker/geppetto-persistence/geppetto.plan /home/developer
COPY geppetto.plan workspace/org.geppetto/

WORKDIR $HOME/workspace
RUN ../copy.sh https://github.com/openworm/org.geppetto.model.git "${targetBranch}" "${originBranch}" "${defaultBranch}" &&\
  cd org.geppetto.model &&\
  /bin/echo -e "\e[96mMaven install org.geppetto.model\e[0m" &&\
  mvn --quiet install &&\
  rm -rf src

RUN ../copy.sh https://github.com/openworm/org.geppetto.core.git "${targetBranch}" "${originBranch}" "${defaultBranch}" &&\
  cd org.geppetto.core &&\
  /bin/echo -e "\e[96mMaven install org.geppetto.core\e[0m" &&\
  mvn --quiet install &&\
  rm -rf src

RUN ../copy.sh https://github.com/openworm/org.geppetto.model.neuroml.git "${targetBranch}" "${originBranch}" "${defaultBranch}" &&\
  cd org.geppetto.model.neuroml &&\
  /bin/echo -e "\e[96mMaven install org.geppetto.model.neuroml\e[0m" &&\
  mvn --quiet install &&\
  rm -rf src

RUN ../copy.sh https://github.com/openworm/org.geppetto.simulation.git "${targetBranch}" "${originBranch}" "${defaultBranch}" &&\
  cd org.geppetto.simulation &&\
  /bin/echo -e "\e[96mMaven install org.geppetto.simulation\e[0m" &&\
  mvn --quiet install &&\
  rm -rf src

RUN ../copy.sh https://github.com/openworm/org.geppetto.frontend.git "${targetBranch}" "${originBranch}" "${defaultBranch}"

RUN cd $HOME/workspace/org.geppetto.frontend/src/main &&\
  $HOME/copy.sh https://github.com/openworm/geppetto-application.git "${targetBranch}" "${originBranch}" "${defaultBranch}" &&\
  mv geppetto-application webapp

RUN cd $HOME/workspace/org.geppetto.frontend/src/main/webapp &&\
  $HOME/rename.sh https://github.com/openworm/geppetto-client.git "${targetBranch}" "${originBranch}" "${defaultBranch}"

RUN cd $HOME/workspace/org.geppetto.frontend &&\
  mvn --quiet install &&\
  rm -rf src

RUN ../copy.sh https://github.com/openworm/org.geppetto.persistence.git "${targetBranch}" "${originBranch}" "${defaultBranch}" &&\
  cd org.geppetto.persistence &&\
  /bin/echo -e "\e[96mMaven install org.geppetto.persistence\e[0m" &&\
  mvn --quiet install

WORKDIR $HOME
#END GET GEPPETTO SOURCES

#INSTALL MYSQL
USER root
ENV MYSQL_USER=mysql \
    MYSQL_DATA_DIR=/var/lib/mysql \
    MYSQL_RUN_DIR=/run/mysqld \
    MYSQL_LOG_DIR=/var/log/mysql

RUN apt-get -o Acquire::Check-Valid-Until=false update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -qq -y mysql-server \
 && rm -rf ${MYSQL_DATA_DIR} \
 && rm -rf /var/lib/apt/lists/*

RUN mkdir -p ${MYSQL_DATA_DIR} && mkdir -p ${MYSQL_RUN_DIR} && \
  mkdir -p ${MYSQL_LOG_DIR}

USER developer

#SETUP MYSQL CONFIG
RUN mkdir -p geppetto/
RUN mkdir rm /home/developer/virgo/./repository/usr
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
# RUN cd /home/developer/workspace/org.geppetto.persistence && mvn install --quiet && mvn install

RUN sudo service mysql start && cd /home/developer/workspace/org.geppetto.persistence && mvn exec:java -Dexec.mainClass="org.geppetto.persistence.util.DBTestData" -Dexec.classpathScope=runtime

#END INSTALL MYSQL
 
RUN cd /home/developer/workspace/org.geppetto/utilities/source_setup && python update_server.py

RUN sudo echo "accessKey=$aKey" > /home/developer/geppetto/aws.credentials
RUN sudo echo "secretKey=$sKey" >> /home/developer/geppetto/aws.credentials

EXPOSE 8080
CMD sudo service mysql start && /home/developer/virgo/bin/startup.sh
