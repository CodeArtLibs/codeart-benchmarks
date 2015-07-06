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
env.venv = 'env'
env.python = 'python2.7'

# Examples of Usage
# fab --list

VERSION = 'python-0.0.19'

# Utilities

def venv():
    return 'source %(env)s/bin/activate' % dict(env=env.venv)

# Tasks

@task
def check():
    env.run('grep -Ir "THE_PROJECT" .')

@task
def bootstrap():
    print(red("Configuring application"))
    env.run('virtualenv %(env)s -p %(python)s' % dict(env=env.venv, python=env.python))
    with prefix(venv()):
        env.run('pip install -r requirements.txt')
        env.run('pip install -r requirements-dev.txt')
    print(green("Bootstrap success"))

@task
def clean():
    env.run('rm -rf ~*')
    env.run('rm -rf *.pyc *.pyo')
    env.run('rm -rf data/')
    env.run('rm -rf *.egg-info')
    env.run('rm -rf dist/')

@task
def install():
    with prefix(venv()):
        env.run('python --version')
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
def package():
    with prefix(venv()):
        env.run('python setup.py sdist')

@task
def first_publish():
    package()
    with prefix(venv()):
        env.run('python setup.py register')
    publish()

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
    with prefix(venv()):
        env.run('python setup.py sdist upload')

@task
def republish():
    reset_tag()
    publish()
