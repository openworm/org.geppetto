FROM slarson/docker-eclipse:luna-java-7

MAINTAINER stephen@openworm.org

#ECLIPSE INSTALL
RUN wget https://dl.dropboxusercontent.com/u/7538688/archive.zip && unzip archive.zip

COPY eclipse.ini.install /opt/eclipse/eclipse.ini

#run once to carryout the install
RUN /usr/local/bin/eclipse

#once, completed, put the run eclipse.ini into place
COPY eclipse.ini.run /opt/eclipse/eclipse.ini

RUN mkdir /home/developer/.m2 && chown developer:developer .m2
VOLUME /home/developer/.m2
#END ECLIPSE installed

#VIRGO INSTALL
RUN apt-get update && apt-get install -y curl bsdtar
RUN curl -L 'http://www.eclipse.org/downloads/download.php?file=/virgo/release/VP/3.6.4.RELEASE/virgo-tomcat-server-3.6.4.RELEASE.zip&mirror_id=580&r=1' | bsdtar --strip-components 1 -C /home/virgo -xzf -
RUN chmod u+x /home/virgo/bin/*.sh
ENV SERVER_HOME /home/virgo
#END VIRGO INSTALL

CMD /usr/local/bin/eclipse
