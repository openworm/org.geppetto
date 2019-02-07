FROM metacell/java-virgo-maven:latest

LABEL maintainer="Facundo Rodriguez <facundo@metacell.us>"

ARG mainBranch=development
ENV mainBranch=${mainBranch}
RUN /bin/echo -e "\e[1;35mUSE GIT BRANCH ------------ $mainBranch\e[0m"    

# get geppetto
RUN mkdir -p workspace &&\
  cd workspace &&\
  ../copy.sh http://github.com/openworm/org.geppetto.git ${mainBranch}

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

RUN git clone https://github.com/openworm/org.geppetto.model.nwb.git &&\
  cd org.geppetto.model.nwb &&\
  git checkout ${mainBranch}; \
  git lfs pull &&\
  mvn -DskipTests install &&\
  rm -rf src .git

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

COPY --chown=1000:1000 GeppettoConfiguration.json $HOME/workspace/org.geppetto.frontend/src/main/webapp/
RUN cd $HOME/workspace/org.geppetto.frontend &&\
  mvn -Dhttps.protocols=TLSv1.2 -DcontextPath=/ -DuseSsl=true -DskipTests install &&\
  rm -rf src

RUN mkdir rm $SERVER_HOME/./repository/usr
COPY --chown=1000:1000 geppetto.plan $HOME/workspace/org.geppetto/
COPY --chown=1000:1000 config.json $HOME/workspace/org.geppetto/utilities/source_setup/
RUN rm $SERVER_HOME/pickup/*.jar
RUN cd $HOME/workspace/org.geppetto/utilities/source_setup && python update_server.py

EXPOSE 8080
CMD [ "/bin/bash", "-c", "$SERVER_HOME/bin/startup.sh" ]
