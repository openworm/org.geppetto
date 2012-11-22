import os
#########################################
# Downloads a Virgo server and the OpenWorm
# bundles and creates a zip file that contains
# a configured Virgo server
# by: Stephen Larson (stephen@openworm.org)
#
# To use:
# * Make sure Fabric is installed:
#   http://docs.fabfile.org/en/1.5/installation.html
# * Set JAVA_HOME and MAVEN_HOME directories below:
os.environ['JAVA_HOME'] = '/usr'
os.environ['MAVEN_HOME'] = '/home/ubuntu/notebooks/apache-maven-2.2.1'
#######################################
from __future__ import with_statement
import urllib
import tempfile, shutil, zipfile, re
from fabric.api import *
import os.path as op

urls = ['http://ftp.osuosl.org/pub/eclipse//virgo/milestone/VP/3.6.0.M01/virgo-tomcat-server-3.6.0.M01.zip']

openwormpackages = ['org.openworm.simulationengine.core', 'org.openworm.simulationengine',
'org.openworm.simulationengine.samplesimulation', 
'org.openworm.simulationengine.frontend',
'org.openworm.simulationengine.samplesolver',
'org.openworm.simulationengine.model.sph',
'org.openworm.simulationengine.solver.sph',
'org.openworm.simulationengine.simulator.sph',
'org.openworm.simulationengine.simulation',
'org.openworm.simulationengine.samplesimulator']

for p in openwormpackages:
    urls = urls + ['https://github.com/openworm/' + p + '/archive/master.zip']
    
print urls

tempdir = tempfile.mkdtemp()

#download and unpack all packages into a temp directory
for u in urls:
    (zFile, x) = urllib.urlretrieve(u)
    vz = zipfile.ZipFile(zFile)
    vz.extractall(tempdir)
    
#make an openworm directory and move the contents of virgo into it
#so the final package has a nice name
with lcd(tempdir):
    print local('mkdir -p package/openworm', capture=True)
    print local('mv virgo-tomcat-server-3.6.0.M01/* package/openworm/', capture=True)

#set server home in temp directory
server_home = op.join(tempdir, 'package/openworm')
os.environ['SERVER_HOME'] = server_home

#use Maven to build all the OpenWorm code bundles 
#and place the contents in the Virgo installation
for p in openwormpackages:
    dirp = op.join(tempdir, p + '-master')
    print '**************************'
    print 'BUILDING ' + dirp
    print '**************************'
    with lcd(dirp):
        with settings(hide('everything'), warn_only=True):
            print local('$MAVEN_HOME/bin/mvn install', capture=True)
            print local('cp target/classes/lib/* $SERVER_HOME/repository/usr/', capture=True)
            print local('cp target/* $SERVER_HOME/repository/usr/', capture=True)

#put the .plan file in the pickup folder        
with lcd(op.join(tempdir, 'org.openworm.simulationengine' + '-master')):
    print local('cp owsefull.plan $SERVER_HOME/pickup/', capture=True)

#fix the properties file
f = open(op.join(server_home, 'repository/ext/org.eclipse.virgo.web.properties'), 'r+')
text = f.read()
text = re.sub('strict', 'defaulted', text)
f.seek(0)
f.write(text)
f.truncate()
f.close()

#set permissions on the bin directory
#these do carry over into the archive
with lcd(server_home):
    print local('chmod -R +x ./bin', capture=True)
    
#zip up the contents of the virgo directory for distribution
archive_name = os.path.expanduser(os.path.join('~', 'openworm-snapshot'))
root_dir = os.path.expanduser(os.path.join(tempdir, 'package'))
snapshot = shutil.make_archive(archive_name, 'zip', root_dir)

print 'Your snapshot is ready: ' + snapshot