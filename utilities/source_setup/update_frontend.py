#!/usr/bin/python

#
#	Deploys the geppetto frontend in staging due to the issue experienced with the new Virgo tooling
#

import os, sys, json, distutils.core, shutil, glob
from subprocess import call

serverHome = os.environ['SERVER_HOME']
config = json.loads(open(os.path.join(os.path.dirname(__file__), 'config.json')).read())
sourcesdir = config['sourcesdir']
repo = {
        "name":"org.geppetto.frontend",
        "url":"https://github.com/openworm/org.geppetto.frontend.git",
        "auto_install":"yes"
    }



def copyext(targetdir, extension):
    files = glob.iglob(os.path.join(targetdir, extension+'-*/*'))
    for file in files:
        if os.path.isfile(file):
            shutil.copy2(file, os.path.join(serverHome, 'stage', repo['name']+'.jar'))

def main(argv):
    print 'Copying Frontend into staging' , repo['name']
    targetdir = os.path.join(sourcesdir, repo['name'], 'target')
    copyext(targetdir, 'frontend')

if __name__ == "__main__":
	main(sys.argv[1:])
