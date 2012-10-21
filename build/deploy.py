#!/usr/bin/env python

from fabricate import *
import shutil
import os
import sys
import subprocess
import boto

HOME_DIR = os.getcwd()

if 'S3CONFIG' not in os.environ:
    print 'S3CONFIG not defined'
    S3CONFIG='./.s3cfg'
else:
    S3CONFIG=os.environ['S3CONFIG']

def cleanup_s3():
    s3 = boto.connect_s3()
    b = s3.get_bucket('hubspoke.github.com')
    keys = b.list()
    for k in keys:
        if not os.path.exists('./target/site/' + k.key):
            k.delete()

def s3deploy():
    cleanup_s3()
    os.chdir('./target/site')
    subprocess.call(['s3cmd', '--config='+S3CONFIG, 'sync', '.', 's3://hubspoke.github.com'])
    os.chdir(HOME_DIR)

def build():
    s3deploy()

main()
