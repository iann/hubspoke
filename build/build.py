#!/usr/bin/env python

from fabricate import *
import shutil
import os

setup(dirs=['..', '../content', '../data'])

def runHyde():
    run('hyde', '-s', '..', 'gen')
    shutil.copytree('../deploy', './target/site')

def clean():
    shutil.rmtree('target', ignore_errors=True)
    os.makedirs('target', 0755)

def build():
    clean()
    runHyde()

main()
