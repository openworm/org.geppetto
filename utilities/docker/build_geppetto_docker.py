from __future__ import with_statement
import tempfile, os, shlex, subprocess

#########################################
# Launches Geppetto via Docker
# Will be running on http://localhost:8080
# by: Stephen Larson (stephen@openworm.org)
# To use:
# * Make sure Docker (http://docker.com) is installed and running
# * Make sure git is installed: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
# * Currently only works on linux-based systems
##########################################

def execute(argv):
    args = shlex.split(raw_cmd)
    subprocess.call(args)

geppettomodules = ['org.geppetto.model',
'org.geppetto.core',
'org.geppetto.model.neuroml',
'org.geppetto.model.swc',
'org.geppetto.simulation',
'org.geppetto.frontend',
'org.geppetto']

os.mkdir("~/virgo/pickup")
os.mkdir("~/virgo/usr")

#use Maven to build all the OpenWorm code bundles
#and place the contents in the Virgo installation
for p in geppettomodules:
    #clone the repo
    subprocess.call(["git", "clone", "https://github.com/openworm/" + p + ".git"])
    os.chdir(p)

    #build the code using a docker image that arrives, does the maven build, and disappears
    execute("docker run -it --rm --name my-maven-project -v '$PWD':/usr/src/mymaven -v ~/.m2:/root/.m2 -w /usr/src/mymaven maven:3.2-jdk-7 mvn clean install")

    #copy files into virgo
    execute("cp target/classes/lib/* ~/virgo/usr")
    execute("cp target/* ~/virgo/usr")

    os.chdir("..")

execute("cp org.geppetto/geppetto.plan ~/virgo/pickup")

os.chdir("utilities/docker/virgo-tomcat-server-3.6.4-RELEASE-jre-7")

execute("docker build -t slarson/virgo-tomcat-server:3.6.4-RELEASE-jre-7 .")

execute("docker run --name='virgo-tomcat-server' --publish=8080:8080 -v ~/virgo/pickup:/home/virgo/pickup -v ~/virgo/usr:/home/virgo/repository/usr -t slarson/virgo-tomcat-server:3.6.4-RELEASE-jre-7")
