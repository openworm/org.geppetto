#!/usr/bin/python

#
#	Deploys built artifacts to $SERVER_HOME/repository/usr
#

import os, sys, json, distutils.core, shutil, glob
from subprocess import call

serverHome = os.environ['SERVER_HOME']
config = json.loads(open(os.path.join(os.path.dirname(__file__), 'config.json')).read())
sourcesdir = config['sourcesdir']



def copyext(targetdir, extension):
	files = glob.iglob(os.path.join(targetdir, '*.'+extension))
	for file in files:
	    if os.path.isfile(file):
	        shutil.copy2(file, os.path.join(serverHome, 'repository', 'usr'))

def main(argv):
    serverHome = os.environ['SERVER_HOME']
    if len(sys.argv)>1 and sys.argv[1]=='eclipse':
        print 'Updating the virgo server, Eclipse is used'
        eclipse=True
    else:
        print 'Updating the virgo server, Eclipse is not used'
        eclipse=False
    for repo in config['repos']:
        print 'Copying libraries for' , repo['name']
        targetdir = os.path.join(sourcesdir, repo['name'], 'target')
        if not eclipse:
            copyext(targetdir, 'jar')
            copyext(targetdir, 'war')
            copyext(targetdir, 'libd')
        copyext(os.path.join(targetdir, 'classes', 'lib'), 'jar')
        copyext(os.path.join(targetdir, 'classes', 'lib'), 'war')
        copyext(os.path.join(targetdir, 'classes', 'lib'), 'libd')

    if not eclipse:
	    shutil.copy2(os.path.join(sourcesdir, 'org.geppetto', 'geppetto.plan'), os.path.join(serverHome, 'pickup'))
    print 'Geppetto build deployed to virgo'

if __name__ == "__main__":
	main(sys.argv[1:])
