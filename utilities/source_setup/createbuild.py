#!/usr/bin/python

#
#   Deploys built artifacts to $SERVER_HOME/repository/usr
#

import os, sys, json, distutils.core, shutil, glob, zipfile
from subprocess import call

config = json.loads(open(os.path.join(os.path.dirname(__file__), 'config.json')).read())
sourcesdir = config['sourcesdir']
buildir = os.path.join(sourcesdir, 'build', 'geppetto')


def copyext(targetdir, extension):
    files = glob.iglob(os.path.join(targetdir, '*.'+extension))
    for file in files:
        if os.path.isfile(file):
            shutil.copy2(file, buildir)

def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            zip.write(filepath, os.path.basename(filepath))

def main(argv):
    
    shutil.rmtree(buildir, ignore_errors=True)     
    os.makedirs(buildir)

    for repo in config['repos']:
        print 'Copying libraries for' , repo['name']
        targetdir = os.path.join(sourcesdir, repo['name'], 'target')

        copyext(targetdir, 'jar')
        copyext(targetdir, 'war')
        copyext(os.path.join(targetdir, 'classes', 'lib'), 'jar')
        copyext(os.path.join(targetdir, 'classes', 'lib'), 'war')


    shutil.copy2(os.path.join(sourcesdir, 'org.geppetto', 'geppetto.plan'), buildir)

    zipf = zipfile.ZipFile(os.path.join(sourcesdir,'build','geppetto.zip'), 'w')
    zipdir(buildir, zipf)
    zipf.close()
    shutil.rmtree(buildir, ignore_errors=True)     
    print 'Geppetto build created at ' + buildir

if __name__ == "__main__":
    main(sys.argv[1:])
