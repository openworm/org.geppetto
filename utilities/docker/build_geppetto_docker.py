from __future__ import with_statement
import tempfile, os, shlex, subprocess, glob, shutil

#########################################
# Launches Geppetto via Docker
# Will be running on http://localhost:8080/org.geppetto.frontend
# by: Stephen Larson (stephen@openworm.org)
# To use:
# * Make sure Docker (http://docker.com) is installed and running
# * Make sure git is installed: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
# * Currently only works on linux-based systems
##########################################

def execute(argv):
    args = shlex.split(argv)
    subprocess.call(args)

geppettomodules = ['org.geppetto.model',
'org.geppetto.core',
'org.geppetto.model.neuroml',
'org.geppetto.model.swc',
'org.geppetto.simulation',
'org.geppetto.frontend']

pwd = os.getcwd()

if not os.path.exists("virgo"):
    os.makedirs("virgo/pickup")
    os.makedirs("virgo/usr")

#use Maven to build all the OpenWorm code bundles
#and place the contents in the Virgo installation
for p in geppettomodules:

    if not os.path.exists(pwd + "/" + p):
      #clone the repo
      subprocess.call(["git", "clone", "https://github.com/openworm/" + p + ".git"])

      #build the code using a docker image that arrives, does the maven build, and disappears
      execute("docker run -it --rm --name my-maven-project -v " + pwd + "/" + p + ":/usr/src/mymaven -v " + pwd + "/.m2:/root/.m2 -w /usr/src/mymaven maven:3.2-jdk-7 mvn clean install")

      #copy files into virgo
      for file in glob.glob(pwd + "/" + p + "/target/classes/lib/*.[a-z]*"):
        shutil.copy(file, pwd+"/virgo/usr")
      for file in glob.glob(pwd + "/" + p + '/target/*.[a-z]*'):
        shutil.copy(file, pwd+"/virgo/usr")

shutil.copy("org.geppetto/geppetto.plan", "virgo/pickup")

execute("docker build -t slarson/virgo-tomcat-server:3.6.4-RELEASE-jre-7 "+pwd+"/org.geppetto/utilities/docker/virgo-tomcat-server-3.6.4-RELEASE-jre-7/")

execute("docker run --name='virgo-tomcat-server' --publish=8080:8080 -v "+pwd+"/virgo/pickup:/home/virgo/pickup -v "+pwd+"/virgo/usr:/home/virgo/repository/usr -t slarson/virgo-tomcat-server:3.6.4-RELEASE-jre-7")
