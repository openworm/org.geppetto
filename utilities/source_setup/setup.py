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
	yes = set(['yes','y'])
	if argv:
		target_dir = argv[0]
	else:
		target_dir = os.path.abspath(config['sourcesdir'])
		
	if not os.path.isdir(target_dir):
		raise IOError("Geppetto sources folder does not exist, create it and set the sourcesdir field in config.json: \"" + target_dir + "\"")
		
	print "Copying Geppetto repositories into", target_dir

	for repo in config['repos']:
		if repo['auto_install'] == "yes":
			print "Geppetto repository automatically cloned", repo['url']
			subprocess.call(['git','clone',repo['url']], cwd = target_dir)
		else:
			print "Geppetto repository not automatically cloned", repo['url']
			print "Would you like to include this repository anyway?"
			repository = raw_input().lower()
			
			if repository in yes:
				subprocess.call(['git','clone',repo['url']], cwd=target_dir)
	print "All Geppetto repositories copied"

if __name__ == "__main__":
	main(sys.argv[1:])
