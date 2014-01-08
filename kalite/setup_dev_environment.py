#!/usr/bin/env python3

import argparse
import json
import subprocess
import time

def main():
    args = setup_args()

    if args.command == 'up':
        docker_common_commands = ['docker', 'run', '-d', '-t', '-i', '-v', '/home/user/src/ka-lite:/ka-lite']

        central_port = '5000'
        dist_port = '4000'

        central_command = docker_common_commands + ['-p', '127.0.0.1:%s:8000' % central_port, '-name', 'central', 'kalite:central']
        central_command += [args.central_command]
        subprocess.call(central_command)

        dist_command = docker_common_commands + ['-p', '127.0.0.1:%s:8000' % dist_port, '-link', 'central:central', '-name', 'dev', 'kalite:dev']
        dist_command += [args.dist_command]
        subprocess.call(dist_command)

    elif args.command == 'down':
        # the IDs we need
        central_info = json.loads(subprocess.check_output(['docker', 'inspect', 'central']).decode('utf-8'))
        dist_info = json.loads(subprocess.check_output(['docker', 'inspect', 'dev']).decode('utf-8'))
        central_id = central_info[0]['ID']
        dist_id = dist_info[0]['ID']

        # ok we're done, cleanup the containers
        print('cleaning up containers')
        subprocess.call(['docker', 'stop', '-t=3', central_id], stdout=subprocess.DEVNULL)
        subprocess.call(['docker', 'rm', central_id])

        subprocess.call(['docker', 'stop', '-t=3', dist_id], stdout=subprocess.DEVNULL)
        subprocess.call(['docker', 'rm', dist_id])


def setup_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('command', type=str, choices=['up', 'down'], help='the command (either up or down)')
    parser.add_argument('--central-command', help='the command to initialize the central server container', default='bash')
    parser.add_argument('--dist-command', help='the command to initialize the dist server container', default='bash')

    return parser.parse_args()


if __name__ == '__main__':
    main()
