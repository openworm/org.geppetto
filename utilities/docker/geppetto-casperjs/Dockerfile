FROM java:7

RUN apt-get update && apt-get install -y sudo xvfb

RUN useradd -ms /bin/bash developer

RUN mkdir -p /home/developer && mkdir -p /etc/sudoers.d \
    echo "developer:x:1000:1000:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:1000:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown developer:developer -R /home/developer && \
    chown root:root /usr/bin/sudo && chmod 4755 /usr/bin/sudo

USER developer
ENV HOME /home/developer
WORKDIR /home/developer

# install node and npm plus update firefox
RUN sudo apt-get install -y nodejs npm
RUN sudo apt-get install -y nodejs-legacy
RUN sudo apt-get install -y xvfb libxrender-dev libasound2 libdbus-glib-1-2 libgtk2.0-0 bzip2
RUN cd /usr/local && sudo wget --no-verbose -O /tmp/firefox-50.0.tar.bz2 http://ftp.mozilla.org/pub/firefox/releases/50.0/linux-x86_64/en-US/firefox-50.0.tar.bz2
RUN sudo tar xvjf /tmp/firefox-50.0.tar.bz2
RUN cd ~ && sudo ln -s firefox-50.0.tar.bz2

# install casperjs needed libraries
RUN sudo npm install --silent -g phantomjs
RUN sudo npm install --silent -g casperjs

# set up dir for running caspers tests
RUN sudo curl -k -O https://download.slimerjs.org/releases/0.10.3/slimerjs-0.10.3.tar.bz2
RUN sudo pwd && tar -xjpvf slimerjs-0.10.3.tar.bz2
RUN sudo rm slimerjs-0.10.3.tar.bz2
WORKDIR /home/developer/workspace/org.geppetto.frontend/src/main/webapp/js/pages/tests/casperjs
RUN casperjs --version
RUN sudo apt-get install -y libgtk-3-dev lshw
ENV SLIMERJSLAUNCHER  /home/developer/firefox/firefox
ENV SLIMERJS_EXECUTABLE /home/developer/slimerjs-0.10.3/slimerjs
ENV LD_LIBRARY_PATH /usr/lib/x86_64-linux-gnu/
RUN sudo apt install -y net-tools
RUN cd /home/developer/slimerjs-0.10.3
RUN  ls -l

RUN xvfb-run -a casperjs test --includes=CoreTestsUtility.js CoreTests.js --engine=slimerjs --debug=yes