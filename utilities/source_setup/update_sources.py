#!/usr/bin/python

#
#	Updates source repos by executing 'git pull'
#

import os, sys, getopt, subprocess, json
from subprocess import call
config = json.loads(open(os.path.join(os.path.dirname(__file__), 'config.json')).read())

def main(argv):
	yes = set(['yes'])

	targetDir = '.' if len(argv) == 0 else argv[0];
	
	print "Would you like to choose which repositories to update?"
	custom_repo = raw_input().lower()
	
        # Note the change to default_repo rather than auto_install

	if custom_repo in yes:
		for repo in config['repos']:
			if repo['default_repo'] == "yes":
				print subprocess.call(['git','pull'], cwd = os.path.join(config['sourcesdir'], repo['name']))
			else:
				print "This repository is not automatically updated"
				print "Would you like to update it anyway?"
				repository = raw_input().lower()

				if repository in yes:
					print subprocess.call(['git','pull'], cwd = os.path.join(config['sourcesdir'], repo['name']))
	else:
		for repo in config['repos']:
			if repo['default_repo'] == "yes":
				print subprocess.call(['git','pull'], cwd = os.path.join(config['sourcesdir'], repo['name']))
	
				
	
	print 'All geppetto repos updated'

if __name__ == "__main__":
	main(sys.argv[1:])
