#!/usr/bin/env python2.7

import fnmatch
import os
import subprocess

def dockerfile_dirs(dir=None):
    if not dir:
        dir = os.path.dirname(os.path.abspath(__file__))

    for path, _, filenames in os.walk(dir):
        if 'Dockerfile' in filenames:
            yield path

def build_tag(name):
    reponame = 'learningequality/kalite'

    if name in ['base', '.', 'kalite']:
        tag = "base"
    else:
        tag = name

    return '-t="%s"' % ':'.join([reponame, tag])


if __name__ == '__main__':
    command = ['sudo', 'docker', 'build']
    for dir in dockerfile_dirs():
        basename = os.path.basename(dir)
        realcommand = command + [build_tag(basename), dir]
        print ' '.join(realcommand)
        subprocess.call(realcommand, stdout=subprocess.PIPE)
