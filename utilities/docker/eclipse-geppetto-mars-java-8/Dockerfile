FROM slarson/docker-eclipse:latest

MAINTAINER stephen@openworm.org

COPY eclipse.ini.install /opt/eclipse/eclipse.ini

#run once to carryout the install
RUN /usr/local/bin/eclipse

#once, completed, put the run eclipse.ini into place
COPY eclipse.ini.run /opt/eclipse/eclipse.ini

RUN mkdir /home/developer/.m2 && chown developer:developer .m2
VOLUME /home/developer/.m2

CMD /usr/local/bin/eclipse
