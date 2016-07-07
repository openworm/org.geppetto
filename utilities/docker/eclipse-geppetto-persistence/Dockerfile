FROM slarson/eclipse-geppetto:luna-java-7

MAINTAINER stephen@openworm.org

USER developer
RUN cd workspace/ && git clone http://github.com/openworm/org.geppetto.persistence \
  && cd org.geppetto.persistence && mvn install

RUN mkdir -p geppetto/
ADD db.properties geppetto/
RUN cd workspace/org.geppetto.persistence && mvn exec:java -Dexec.mainClass="org.geppetto.persistence.util.DBTestData" -Dexec.classpathScope=runtime

CMD /usr/local/bin/eclipse
