#!/usr/bin/env python3

import fnmatch
import optparse
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

    return '-t={}'.format(':'.join([reponame, tag]))


if __name__ == '__main__':
    # get cmdline arguments
    optparser = optparse.OptionParser()
    optparser.add_option('-v', '--verbose',
                         dest='verbose',
                         action='store_true',
                         default=False,
                         help='show docker build output to stdout.')
    options, _ = optparser.parse_args()

    command = ['sudo', 'docker', 'build', '-rm=true']
    for dir in dockerfile_dirs():
        basename = os.path.basename(dir)
        realcommand = command + [build_tag(basename), dir]
        print(' '.join(realcommand))

        if options.verbose:
            stdout=None
        else:
            stdout=subprocess.DEVNULL

        subprocess.call(realcommand, stdout=stdout)
