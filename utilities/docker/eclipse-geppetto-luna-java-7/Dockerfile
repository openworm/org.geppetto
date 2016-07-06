FROM slarson/docker-eclipse:luna-java-7

MAINTAINER stephen@openworm.org

COPY eclipse.ini.install /opt/eclipse/eclipse.ini

#run once to carryout the install
RUN /usr/local/bin/eclipse

#once, completed, put the run eclipse.ini into place
COPY eclipse.ini.run /opt/eclipse/eclipse.ini

VOLUME /home/developer/.m2

CMD /usr/local/bin/eclipse
