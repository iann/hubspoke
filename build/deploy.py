#!/usr/bin/env python

from fabricate import *
import shutil
import os
import sys
import subprocess

HOME_DIR = os.getcwd()

if 'S3CONFIG' not in os.environ:
    print 'S3CONFIG not defined'
    S3CONFIG='./.s3cfg'
else:
    S3CONFIG=os.environ['S3CONFIG']

def s3deploy():
    os.chdir('./target/site')
    subprocess.call(['s3cmd', '--config='+S3CONFIG, 'sync', '.', 's3://hubspoke.github.com'])
    os.chdir(HOME_DIR)

def build():
    s3deploy()

main()
