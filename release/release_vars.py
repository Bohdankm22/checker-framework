#!/usr/bin/env python
# encoding: utf-8
"""
release_vars.py

Created by Jonathan Burke on 2013-02-05.

Copyright (c) 2012 University of Washington. All rights reserved.
"""

# See release_development.html for an explanation of how the release process works
# it will be invaluable when trying to understand the scripts that drive the
# release process

#from release_utils import *
import os
import datetime
import pwd

#---------------------------------------------------------------------------------
#The only methods that should go here are methods that help define global release
#variables.  All other methods that aid in release should go in release_utils.py

def getAndAppend(name, append):
    if os.environ.has_key(name):
        return os.environ[name] + append

    else:
        return ""

def append_to_PATH(paths):
    current_PATH = os.getenv('PATH')
    new_PATH = current_PATH + ':' + ':'.join(paths)
    os.environ['PATH'] = new_PATH

#---------------------------------------------------------------------------------

#Maximum allowable size of files when downloading, 2gi
MAX_DOWNLOAD_SIZE=2000000000

#The location the test site is built in
HTTP_PATH_TO_DEV_SITE  = "http://http://types.cs.washington.edu/dev"
FILE_PATH_TO_DEV_SITE  = "/cse/www2/types/dev/"

#The location the test site is pushed to when it is ready
HTTP_PATH_TO_LIVE_SITE  = "http://types.cs.washington.edu"
FILE_PATH_TO_LIVE_SITE  = "/cse/www2/types"

#Location in which we will download files to run sanity checks
SANITY_DIR = "/scratch/jsr308-release/sanity"

#Every time a release is built the changes/tags are pushed here
#When a release is deployed all INTERM repos get pushed to LIVE_REPOS
INTERM_REPO_ROOT    = "/scratch/jsr308-release/interm"
INTERM_CHECKER_REPO = os.path.join(INTERM_REPO_ROOT, "checker-framework")
INTERM_JSR308_REPO  = os.path.join(INTERM_REPO_ROOT, "jsr308-langtools")
INTERM_ANNO_REPO    = os.path.join(INTERM_REPO_ROOT, "annotation-tools")

#The central repositories for Checker Framework related projects
LIVE_REPO_ROOT    = "https://code.google.com/p/"
LIVE_CHECKER_REPO = LIVE_REPO_ROOT + "checker-framework"
LIVE_JSR308_REPO  = LIVE_REPO_ROOT + "jsr308-langtools"
LIVE_ANNO_REPO    = LIVE_REPO_ROOT + "annotation-tools"
LIVE_PLUME_LIB    = LIVE_REPO_ROOT + "plume-lib"
LIVE_PLUME_BIB    = LIVE_REPO_ROOT + "plume-bib"

# "USER = os.getlogin()" does not work; see http://bugs.python.org/issue584566
# Another alternative is: USER = os.getenv('USER')
USER = pwd.getpwuid(os.geteuid())[0]

OPENJDK_RELEASE_SITE = 'http://jdk8.java.net/download.html'

EMAIL_TO='jsr308-discuss@googlegroups.com, checker-framework-discuss@googlegroups.com'

#Location of the project directories in which we will build the actual projects
#When we build these projects are pushed to the INTERM repositories
BUILD_DIR        = "/scratch/jsr308-release/build/"
CHECKER_FRAMEWORK = os.path.join(BUILD_DIR, 'checker-framework')
CHECKER_FRAMEWORK_RELEASE = os.path.join(CHECKER_FRAMEWORK, 'release')
CHECKER_BIN_DIR    = os.path.join(CHECKER_FRAMEWORK, 'checkers', 'binary')
CHECKERS_BINARY    = os.path.join(CHECKER_BIN_DIR, 'checkers.jar'       )
CHECKERS_QUALS     = os.path.join(CHECKER_BIN_DIR, 'checkers-quals.jar' )
JAVAC_BINARY       = os.path.join(CHECKER_BIN_DIR, 'javac.jar')
JDK7_BINARY        = os.path.join(CHECKER_BIN_DIR, 'jdk7.jar' )

CHECKERS_BINARY_POM  = os.path.join(CHECKER_BIN_DIR, 'poms', 'checkersPom.xml'      )
CHECKERS_QUALS_POM   = os.path.join(CHECKER_BIN_DIR, 'poms', 'checkersQualsPom.xml' )
JAVAC_BINARY_POM     = os.path.join(CHECKER_BIN_DIR, 'poms', 'compilerPom.xml'      )
JDK7_BINARY_POM      = os.path.join(CHECKER_BIN_DIR, 'poms', 'jdk7Pom.xml'          )

CHECKERS_CHANGELOG = os.path.join(CHECKER_FRAMEWORK, 'checkers', 'changelog-checkers.txt')

JSR308_LANGTOOLS    = os.path.join(BUILD_DIR, 'jsr308-langtools')
JSR308_LT_DOC       = os.path.join(JSR308_LANGTOOLS, 'doc')
JSR308_CHANGELOG    = os.path.join(JSR308_LANGTOOLS, 'doc', 'changelog-jsr308.txt')
JSR308_MAKE         = os.path.join(JSR308_LANGTOOLS, 'make')

ANNO_TOOLS          = os.path.join(BUILD_DIR, 'annotation-tools')
ANNO_FILE_UTILITIES = os.path.join(ANNO_TOOLS,  'annotation-file-utilities')

PLUME_LIB = os.path.join(BUILD_DIR, 'plume-lib')
PLUME_BIB = os.path.join(BUILD_DIR, 'plume-bib')

MAVEN_PLUGIN_DIR = os.path.join(CHECKER_FRAMEWORK, 'maven-plugin')
MAVEN_PLUGIN_POM = os.path.join(MAVEN_PLUGIN_DIR,  'pom.xml')
MAVEN_DEV_REPO  = 'file:///cse/www2/types/dev/m2-repo'
MAVEN_LIVE_REPO = 'file:///cse/www2/types/m2-repo'

RELEASE_REPOS = ( CHECKER_FRAMEWORK,   JSR308_LANGTOOLS,   ANNO_TOOLS )
INTERM_REPOS  = ( INTERM_CHECKER_REPO, INTERM_JSR308_REPO, INTERM_ANNO_REPO )
LIVE_REPOS    = ( LIVE_CHECKER_REPO,   LIVE_JSR308_REPO,   LIVE_ANNO_REPO   )

INTERM_TO_RELEASE_REPOS = (
  ( INTERM_CHECKER_REPO, CHECKER_FRAMEWORK ),
  ( INTERM_JSR308_REPO,  JSR308_LANGTOOLS  ),
  ( INTERM_ANNO_REPO,    ANNO_TOOLS        )
)

LIVE_TO_INTERM_REPOS = (
  ( LIVE_CHECKER_REPO, INTERM_CHECKER_REPO ),
  ( LIVE_JSR308_REPO,  INTERM_JSR308_REPO  ),
  ( LIVE_ANNO_REPO,    INTERM_ANNO_REPO    )
)

JSR308_INTERM_RELEASES_DIR  = os.path.join( FILE_PATH_TO_DEV_SITE, "jsr308",                    "releases" )
AFU_INTERM_RELEASES_DIR     = os.path.join( FILE_PATH_TO_DEV_SITE, "annotation-file-utilities", "releases" )
CHECKER_INTERM_RELEASES_DIR = os.path.join( FILE_PATH_TO_DEV_SITE, "checker-framework",         "releases" )

JSR308_LIVE_RELEASES_DIR  = os.path.join( FILE_PATH_TO_LIVE_SITE, "jsr308",                     "releases" )
AFU_LIVE_RELEASES_DIR     = os.path.join( FILE_PATH_TO_LIVE_SITE, "annotation-file-utilities",  "releases" )
CHECKER_LIVE_RELEASES_DIR = os.path.join( FILE_PATH_TO_LIVE_SITE, "checker-framework",          "releases" )

CURRENT_DATE=datetime.date.today()

#Environment variables for tools needed during the build
os.environ['PLUME_LIB'] =  PLUME_LIB
os.environ['BIBINPUTS']=  '.:' + PLUME_BIB
os.environ['TEXINPUTS'] =  '.:/scratch/secs-jenkins/tools/hevea-1.10/lib/hevea:/usr/share/texmf/tex/latex/hevea/:/homes/gws/mernst/tex/sty:/homes/gws/mernst/tex:..:'
os.environ['PERLLIB']   =  getAndAppend('PERLLIB', ":")  + "/homes/gws/mernst/bin/src/perl/lib/perl5/site_perl/5.10.0:/homes/gws/jburke/perl_lib"
os.environ['PERL5LIB']  =  getAndAppend('PERL5LIB', ":") + "/homes/gws/mernst/bin/src/perl/lib/perl5/site_perl/5.10.0:/homes/gws/jburke/perl_lib"
os.environ['JAVA_7_HOME'] =  '/scratch/secs-jenkins/java/jdk1.7.0'
os.environ['JAVA_8_HOME'] =  '/scratch/jsr308-release/java/jdk1.8.0'
os.environ['JAVA_HOME']   =  os.environ['JAVA_7_HOME']

EDITOR = os.getenv('EDITOR')
if EDITOR == None:
    EDITOR = 'emacs'

HGUSER = os.getenv('HGUSER')
if HGUSER == None:
    raise Exception('HGUSER environment variable is not set')

#This is to catch anyone who blindly copied our directions on setting
#the HGUSER variable in the README-maintainers.html directions
if HGUSER == "yourHgUserName":
    raise Exception('You must replace "yourHgUser" with your own actual HGUSER')

PATH = os.environ['JAVA_HOME'] + "/bin:/scratch/secs-jenkins/tools/hevea-1.10/bin/:" + os.environ['PATH']
PATH = PATH + ":/usr/bin:/projects/uns/F11/bin/:/projects/uns/F11/bin/"
PATH = PATH + ":" + PLUME_LIB + "/bin:/homes/gws/mernst/bin/share"
PATH = PATH + ":/homes/gws/mernst/bin/Linux-i686:/uns/bin:."
os.environ['PATH'] = PATH

#Tools that must be on your PATH ( besides common *nix ones like grep )
TOOLS = [ 'hevea', 'perl', 'java', 'dia', 'latex', 'mvn', 'hg', EDITOR ]

#Script option constants
LT_OPT   = "langtools"
AFU_OPT  = "annotation-file-utilities"
CF_OPT   = "checker-framework"
ALL_OPT  = "all"

PROJECTS_TO_SHORTNAMES  = [ (LT_OPT,  "lt" ),
                            (AFU_OPT, "afu"),
                            (CF_OPT,  "cf" ) ]