#!/usr/bin/env python

from fabricate import *
import shutil
import os
import subprocess

HOME_DIR = os.getcwd()

def s3deploy():
    os.chdir('./target/site')
    subprocess.call(['s3cmd', 'sync', '.', 's3://hubspoke.github.com'])
    os.chdir(HOME_DIR)

def build():
    s3deploy()

main()
