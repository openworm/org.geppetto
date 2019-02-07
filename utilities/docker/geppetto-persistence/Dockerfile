FROM metacell/java-virgo-maven:latest
LABEL maintainer Stephen Larson "slarson@openworm.org"

ARG aKey
ENV aKey=${aKey}
ARG sKey
ENV sKey=${sKey}
ARG mainBranch=development
ENV mainBranch=${mainBranch}
RUN /bin/echo -e "\e[1;35mUSE GIT BRANCH ------------ $mainBranch\e[0m"

# get geppetto
RUN mkdir -p workspace &&\
  cd workspace &&\
  ../copy.sh http://github.com/openworm/org.geppetto.git ${mainBranch}

COPY config.json workspace/org.geppetto/utilities/source_setup/
RUN sudo mv /home/developer/workspace/org.geppetto/utilities/docker/geppetto-persistence/geppetto.plan /home/developer
COPY geppetto.plan workspace/org.geppetto/

WORKDIR $HOME/workspace

RUN ../copy.sh https://github.com/openworm/org.geppetto.model.git ${mainBranch} &&\
  cd org.geppetto.model &&\
  mvn -Dhttps.protocols=TLSv1.2 install &&\
  rm -rf src

RUN ../copy.sh https://github.com/openworm/org.geppetto.core.git ${mainBranch} &&\
  cd org.geppetto.core &&\
  mvn -Dhttps.protocols=TLSv1.2 install &&\
  rm -rf src

RUN ../copy.sh https://github.com/openworm/org.geppetto.model.neuroml.git ${mainBranch} &&\
  cd org.geppetto.model.neuroml &&\
  mvn -Dhttps.protocols=TLSv1.2 install &&\
  rm -rf src

RUN ../copy.sh https://github.com/openworm/org.geppetto.simulation.git ${mainBranch} &&\
  cd org.geppetto.simulation &&\
  mvn -Dhttps.protocols=TLSv1.2 install &&\
  rm -rf src

RUN ../copy.sh https://github.com/openworm/org.geppetto.frontend.git ${mainBranch}

RUN cd $HOME/workspace/org.geppetto.frontend/src/main &&\
  git clone https://github.com/openworm/geppetto-application.git webapp &&\
  cd webapp &&\
  git checkout $mainBranch;\
  rm -rf .git

# check if $mainBranch exist in geppetto-client and modify package.json in case it does
RUN /bin/bash -c "cd $HOME/workspace/org.geppetto.frontend/src/main/webapp &&\
  git ls-remote --heads --tags https://github.com/openworm/geppetto-client.git \
  | grep -E 'refs/(heads|tags)/$mainBranch' > /dev/null &&\
  if [[ '$?' -eq '0' ]]; then \
    sed -ie 's/\"@geppettoengine.*/\"@geppettoengine\/geppetto-client\": \"openworm\/geppetto-client#'${mainBranch}'\"/g' package.json &&\
    echo 'checking out ${mainBranch} for geppetto-client' ; \
  fi"

RUN cd $HOME/workspace/org.geppetto.frontend &&\
  mvn -Dhttps.protocols=TLSv1.2 install &&\
  rm -rf src

WORKDIR $HOME

RUN cd workspace &&\
  git clone https://github.com/openworm/org.geppetto.persistence.git &&\
  cd org.geppetto.persistence &&\
  git checkout $mainBranch ;\
  mvn --quiet install;

#END GET GEPPETTO SOURCES

#INSTALL MYSQL
USER root
ENV MYSQL_USER=mysql \
    MYSQL_DATA_DIR=/var/lib/mysql \
    MYSQL_RUN_DIR=/run/mysqld \
    MYSQL_LOG_DIR=/var/log/mysql

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -qq -y mysql-server net-tools\
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
RUN cd /home/developer/workspace/org.geppetto.persistence && mvn install --quiet && mvn install

RUN sudo service mysql start && cd /home/developer/workspace/org.geppetto.persistence && mvn exec:java -Dexec.mainClass="org.geppetto.persistence.util.DBTestData" -Dexec.classpathScope=runtime

#END INSTALL MYSQL
 
RUN cd /home/developer/workspace/org.geppetto/utilities/source_setup && python update_server.py

RUN sudo echo "accessKey=$aKey" > /home/developer/geppetto/aws.credentials
RUN sudo echo "secretKey=$sKey" >> /home/developer/geppetto/aws.credentials

EXPOSE 8080
CMD sudo service mysql start && /home/developer/virgo/bin/startup.sh
