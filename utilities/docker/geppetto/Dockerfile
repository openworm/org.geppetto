FROM java:7

# Install maven
RUN apt-get update

RUN sudo apt-get install gdebi
RUN wget http://ppa.launchpad.net/natecarlson/maven3/ubuntu/pool/main/m/maven3/maven3_3.2.1-0~ppa1_all.deb
RUN sudo gdebi maven3_3.2.1-0~ppa1_all.deb
RUN sudo ln -s /usr/share/maven3/bin/mvn /usr/bin/maven

RUN mvn --version

