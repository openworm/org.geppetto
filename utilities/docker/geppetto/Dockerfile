FROM slarson:virgo-tomcat-server:3.6.4-RELEASE-jre-7
MAINTAINER Stephen Larson <stephen@openworm.org>
LABEL Description="Geppetto 3.3.0 running on Virgo Tomcat Server 3.6.4-RELEASE running on Java 7"

#Previous to doing the docker build on this Dockerfile, we'll need to have built geppetto
# and packed its contents into the appropriate usr and pickup directories.
#COPY [the virgo/usr and virgo/pickup directories that have been built into this directory]

EXPOSE 8080

USER virgo
CMD ["/home/virgo/bin/startup.sh"]
