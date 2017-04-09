from __future__ import with_statement
import tempfile, os, shlex, subprocess, glob, shutil

#########################################
# Checks out the relevant code, making a workspace
# by: Stephen Larson (stephen@openworm.org)
# To use:
# * Make sure git is installed: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
# * Currently only works on linux-based systems
#
# Things that don't need to be installed locally for this to work:
# * Any third-party python libraries
##########################################

geppettomodules = ['org.geppetto.model',
'org.geppetto.core',
'org.geppetto.model.neuroml',
'org.geppetto.model.swc',
'org.geppetto.simulation',
'org.geppetto.frontend',
'org.geppetto']

pwd = os.getcwd()

#use Maven to build all the OpenWorm code bundles
#and place the contents in the Virgo installation
for p in geppettomodules:

    if not os.path.exists(pwd + "/" + p):
      #clone the repo
      subprocess.call(["git", "clone", "https://github.com/openworm/" + p + ".git"])
