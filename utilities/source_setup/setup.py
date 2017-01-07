#!/usr/bin/python
#
#	Script to clone Geppetto git repositories
#	If a target directory is not passed as the
#	first argument, the sourcesdir specified in
#	config.json is used
#	If config.json is used, org.geppetto.core,
#	model, frontend and simulation are
#	included automatically.
#	The user can chose to select the rest of the repos
#	or automatically include those listed in config,json
#

import os, sys, subprocess, json
try:
   import simplejson
except:
   import json as simplejson
from subprocess import call
from xml.dom.minidom import parse, parseString

print open(os.path.join(os.path.dirname(__file__), 'config.json')).read().decode('utf-8')
config = json.loads(open(os.path.join(os.path.dirname(__file__), 'config.json')).read())

def writeToPomXML(repo):
	#Open pom.xml
	basepath = os.path.dirname(__file__)
	pompath = os.path.abspath(os.path.join(basepath, "..", "..", "pom.xml"))
	
	#Create minidom parser
	pom = parse(pompath)

	#Get elements tagged module - we will need to add to these later.
	modules = pom.getElementsByTagName("modules").item(0)
	all_modules = pom.getElementsByTagName("modules")
	module = pom.getElementsByTagName("module")

	#Start from the assumption that we need to write the repo to our xml file. Check pom.xml to see if the repo is present. 
	# If it is not, add a new element in there with the repo name.
	write_repo = False
	for node in all_modules:
		module_list=node.getElementsByTagName('module')
		for m in module_list:
			if m.childNodes[0].nodeValue == "../"+repo['name']:
				write_repo=True
			print m.childNodes[0].nodeValue
		if write_repo == False:
			new_module = pom.createElement("module")
			new_module.nodeValue="../"+repo['name']
			txt=pom.createTextNode("../"+repo['name'])
			new_module.appendChild(txt)
			modules.appendChild(new_module)
			newline = pom.createTextNode('\n')
			modules.appendChild(newline)
			pom.writexml(open(pompath,"w"),
					indent="	",
					addindent="	",
					newl='')
def writeToPlan(repo):
	#Open geppetto.plan
	basepath = os.path.dirname(__file__)
	planpath = os.path.abspath(os.path.join(basepath, "..", "..", "geppetto.plan")) 
	
	#Create minidom parser
	plan = parse(planpath)
	
	#Get elements tagged plan and artifact.
	plan_name = plan.getElementsByTagName("plan").item(0)
	artifact_type = plan.getElementsByTagName("artifact")
	
	#Start from the assumption that we need to write the repo to our xml file. Check pom.xml to see if the repo is present. 
	#If it is not, add a new element in there with the repo name, bundle type and the repo version.
	write_artifact=False
	artifact_version = artifact_type[0].attributes["version"].value
	for x in range(0, len(artifact_type)): 
		art_ref = artifact_type[x]
		if art_ref.attributes["name"].value == repo['name']:	
 			write_artifact=True
	if write_artifact == False:
		new_artifact = plan.createElement("artifact")
		new_artifact.setAttribute("type", "bundle")
		new_artifact.setAttribute("name", repo["name"])
		new_artifact.setAttribute("version", artifact_version)
		plan_name.appendChild(new_artifact)
		plan.writexml(open(planpath,"w"),
			indent="	",
			addindent="	",
			newl='\n')


def main(argv):
	yes = set(['yes','y'])
	if argv:
		target_dir = argv[0]
	else:
		target_dir = os.path.abspath(config['sourcesdir'])
		
	if not os.path.isdir(target_dir):
		raise IOError("Geppetto sources folder does not exist, create it and set the sourcesdir field in config.json: \"" + target_dir + "\"")
		
	print "Copying Geppetto repositories into", target_dir
	
	print "Would you like to customise your repositories?"
	custom_repo = raw_input().lower()

	if custom_repo in yes:
		for repo in config['repos']:
			if repo['auto_install'] == "yes":
				print "Geppetto repository cloned by default", repo['url']
				subprocess.call(['git','clone',repo['url']], cwd = target_dir)
				#Once the repos are cloned, write to pom.xml
				writeToPomXML(repo)	
				writeToPlan(repo)			
			else:
				print "Geppetto repository not cloned by default", repo['url']
				print "Would you like to clone this repository? [y/n]"
				repository = raw_input().lower()
			
				if repository in yes:
					subprocess.call(['git','clone',repo['url']], cwd=target_dir)
					writeToPomXML(repo)
					writeToPlan(repo)
	
	else:
		for repo in config['repos']:
			if repo['auto_install'] == "yes":
				print "Geppetto repository cloned by default", repo['url']
				subprocess.call(['git','clone',repo['url']], cwd = target_dir)
				#Once the repos are cloned, write to pom.xml
				writeToPomXML(repo)	
				writeToPlan(repo)			
		
			
	#Then add the new repo into geppetto.plan and pom.xml
	print "All Geppetto repositories cloned"

if __name__ == "__main__":
	main(sys.argv[1:])
