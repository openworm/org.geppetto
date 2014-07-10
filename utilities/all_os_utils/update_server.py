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

	for repo in config['repos']:
		targetdir = os.path.join(sourcesdir, repo['name'], 'target')
		copyext(targetdir, 'jar')
		copyext(targetdir, 'war')
		copyext(os.path.join(targetdir, 'classes', 'lib'), 'jar')
		copyext(os.path.join(targetdir, 'classes', 'lib'), 'war')

	shutil.copy2(os.path.join(sourcesdir, 'org.geppetto', 'geppetto.plan'), os.path.join(serverHome, 'pickup'))
	print 'Geppetto build deployed to virgo'

if __name__ == "__main__":
	main(sys.argv[1:])
