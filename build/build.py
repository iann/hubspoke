#!/usr/bin/env python

from fabricate import *
import shutil
import os

def runHyde():
    args = ['-s', '..', 'gen']
    shell('hyde', args, silent=False)
    shutil.move('../deploy', './target/hyde_generated')

def clean():
    shutil.rmtree('target', ignore_errors=True)
    os.makedirs('target', 0755)

def build():
    clean()
    runHyde()

main()
