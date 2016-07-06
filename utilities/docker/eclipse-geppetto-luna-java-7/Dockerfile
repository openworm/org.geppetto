FROM slarson/docker-eclipse:luna-java-7

MAINTAINER stephen@openworm.org

RUN wget https://dl.dropboxusercontent.com/u/7538688/archive.zip && unzip archive.zip

COPY eclipse.ini.install /opt/eclipse/eclipse.ini

#run once to carryout the install
RUN /usr/local/bin/eclipse

#once, completed, put the run eclipse.ini into place
COPY eclipse.ini.run /opt/eclipse/eclipse.ini

RUN mkdir /home/developer/.m2
VOLUME /home/developer/.m2

CMD /usr/local/bin/eclipse
