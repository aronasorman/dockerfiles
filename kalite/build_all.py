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
    reponame = 'kalite'

    if name in ['base', '.', 'kalite']:
        tag = "base"
    else:
        tag = name

    return '-t={}'.format(':'.join([reponame, tag]))

def build_dir(dir):
    command = ['docker', 'build', '-rm=true']
    basename = os.path.basename(dir)
    realcommand = command + [build_tag(basename), dir]
    print(' '.join(realcommand))

    if options.verbose:
        stdout=None
    else:
        stdout=subprocess.DEVNULL

    subprocess.call(realcommand, stdout=stdout)

if __name__ == '__main__':
    # get cmdline arguments
    optparser = optparse.OptionParser()
    optparser.add_option('-v', '--verbose',
                         dest='verbose',
                         action='store_true',
                         default=False,
                         help='show docker build output to stdout.')
    options, args = optparser.parse_args()

    dirs_to_build = dockerfile_dirs()

    # if args are given, build only those directories given in args
    if args:
        dirlist = list(dirs_to_build)
        for dir in args:
            fulldir = os.path.join(os.path.dirname(os.path.abspath(__file__)), dir)
            if fulldir in dirlist:
                build_dir(dir)
    else:                       # build all directories we have here
        for dir in dockerfile_dirs():
            build_dir(dir)
