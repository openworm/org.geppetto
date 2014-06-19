#!/usr/bin/python
#
#	Script to clone Geppetto git repositories
#	If a target directory is not passed as the
#	first argument, the sourcesdir specified in
#	config.json is used
#

import os, sys, subprocess, json
from subprocess import call

config = json.loads(open(os.path.join(os.path.dirname(__file__), 'config.json')).read())

def main(argv):
	targetDir = config['sourcesdir'] if len(argv) == 0 else argv[0];

	for repo in config['repos']:
		subprocess.call(['git','clone',repo['url']], cwd = targetDir)

	print 'All geppetto repos copied'

if __name__ == "__main__":
	main(sys.argv[1:])
