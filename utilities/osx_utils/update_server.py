#!/usr/bin/python

#
#	Deploys built artifacts to $SERVER_HOME/repository/usr
#

import os, sys, json, distutils.core, shutil, glob
from subprocess import call

serverHome = os.environ['SERVER_HOME']
config = json.loads(open('./config.json').read())
sourcesdir = config['sourcesdir']

def copyext(targetdir, extension):
	files = glob.iglob(os.path.join(targetdir,'*.'+extension))
	for file in files:
	    if os.path.isfile(file):
	        shutil.copy2(file, serverHome+'/repository/usr/')

def main(argv):
	targetDir = '.' if len(argv) == 0 else argv[0];
	serverHome = os.environ['SERVER_HOME']

	for repo in config['repos']:
		targetdir = os.path.join(os.path.realpath(sourcesdir+'/'+repo['name']+'/target'))
		copyext(targetdir, 'jar')
		copyext(targetdir, 'war')
		copyext(targetdir+'/classes/lib', 'jar')
		copyext(targetdir+'/classes/lib', 'war')

	shutil.copy2(os.path.realpath(sourcesdir+'/org.geppetto/geppetto.plan'), serverHome+'/pickup')
	print 'Geppetto build deployed to virgo'

if __name__ == "__main__":
	main(sys.argv[1:])
