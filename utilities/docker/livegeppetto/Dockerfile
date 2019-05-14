FROM metacell/java-virgo-maven:development

LABEL maintainer="Facundo Rodriguez <facundo@metacell.us>"

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

WORKDIR $HOME/workspace
RUN ../copy.sh https://github.com/openworm/org.geppetto.model.git "${targetBranch}" "${originBranch}" "${defaultBranch}" &&\
  cd org.geppetto.model &&\
  /bin/echo -e "\e[96mMaven install org.geppetto.model\e[0m" &&\
  mvn -DskipTests --quiet install &&\
  rm -rf src

RUN ../copy.sh https://github.com/openworm/org.geppetto.core.git "${targetBranch}" "${originBranch}" "${defaultBranch}" &&\
  cd org.geppetto.core &&\
  /bin/echo -e "\e[96mMaven install org.geppetto.core\e[0m" &&\
  mvn -DskipTests --quiet install &&\
  rm -rf src

RUN ../copy.sh https://github.com/openworm/org.geppetto.model.neuroml.git "${targetBranch}" "${originBranch}" "${defaultBranch}" &&\
  cd org.geppetto.model.neuroml &&\
  /bin/echo -e "\e[96mMaven install org.geppetto.model.neuroml\e[0m" &&\
  mvn -DskipTests --quiet install &&\
  rm -rf src

RUN ../copy.sh https://github.com/openworm/org.geppetto.model.nwb.git "${targetBranch}" "${originBranch}" "${defaultBranch}" &&\
  cd org.geppetto.model.nwb &&\
  /bin/echo -e "\e[96mMaven install org.geppetto.model.nwb\e[0m" &&\
  mvn -DskipTests --quiet install &&\
  rm -rf src

RUN ../copy.sh https://github.com/openworm/org.geppetto.simulation.git "${targetBranch}" "${originBranch}" "${defaultBranch}" &&\
  cd org.geppetto.simulation &&\
  /bin/echo -e "\e[96mMaven install org.geppetto.simulation\e[0m" &&\
  mvn -DskipTests --quiet install &&\
  rm -rf src

RUN ../copy.sh https://github.com/openworm/org.geppetto.frontend.git "${targetBranch}" "${originBranch}" "${defaultBranch}"

RUN cd $HOME/workspace/org.geppetto.frontend/src/main &&\
  $HOME/copy.sh https://github.com/openworm/geppetto-application.git "${targetBranch}" "${originBranch}" "${defaultBranch}" &&\
  mv geppetto-application webapp

RUN cd $HOME/workspace/org.geppetto.frontend/src/main/webapp &&\
  $HOME/rename.sh https://github.com/openworm/geppetto-client.git "${targetBranch}" "${originBranch}" "${defaultBranch}"

COPY --chown=1000:1000 GeppettoConfiguration.json $HOME/workspace/org.geppetto.frontend/src/main/webapp/
RUN cd $HOME/workspace/org.geppetto.frontend &&\
  /bin/echo -e "\e[96mMaven install org.geppetto.frontend\e[0m" &&\
  mvn -Dhttps.protocols=TLSv1.2 -DcontextPath=/ -DuseSsl=true -DskipTests --quiet install &&\
  rm -rf src

WORKDIR $HOME
RUN mkdir rm $SERVER_HOME/./repository/usr
COPY --chown=1000:1000 geppetto.plan $HOME/workspace/org.geppetto/
COPY --chown=1000:1000 config.json $HOME/workspace/org.geppetto/utilities/source_setup/
RUN rm $SERVER_HOME/pickup/*.jar
RUN cd $HOME/workspace/org.geppetto/utilities/source_setup && python update_server.py

EXPOSE 8080
CMD [ "/bin/bash", "-c", "$SERVER_HOME/bin/startup.sh" ]
