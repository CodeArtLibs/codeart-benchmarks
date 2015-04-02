# coding: utf-8
from __future__ import with_statement
import codecs
import json
import os
import platform
import subprocess
import sys

from fabric.api import *
from fabric.colors import *
from fabric.utils import abort
from fabric.contrib.console import confirm

env.run = local
env.sudo = local

# Examples of Usage
# fab --list

VERSION = '0.0.1'

@task
def check():
    env.run('grep -Ir "THE_PROJECT" .')

@task
def clean():
    env.run('rm -rf ~*')
    env.run('rm -rf *.pyc *.pyo')
    env.run('rm -rf data/')
    env.run('rm -rf *.egg-info')
    env.run('rm -rf dist/')

@task
def install():
    env.run('python --version')
    env.run('ruby --version')
    env.run('easy_install pip')

@task
def tag():
    env.run('git tag %s' % VERSION)
    env.run('git push origin %s' % VERSION)

@task
def reset_tag():
    env.run('git tag -d %s' % VERSION)
    env.run('git push origin :refs/tags/%s' % VERSION)

@task
def publish():
    tag()
    # http://guide.python-distribute.org/quickstart.html
    # python setup.py sdist
    # python setup.py register
    # Create a .pypirc file in ~ dir (cp .pypirc ~)
    # python setup.py sdist upload
    # Manual upload to PypI
    # http://pypi.python.org/pypi/THE-PROJECT
    # Go to 'edit' link
    # Update version and save
    # Go to 'files' link and upload the file
    virtual_env('python setup.py sdist upload', 'env2.7')
