#!/usr/bin/env python3

import json
import subprocess
import time

if __name__ == '__main__':
    docker_common_commands = ['docker', 'run', '-t', '-i', '-v', '/home/user/src/ka-lite:/ka-lite']

    central_port = '5000'
    dist_port = '4000'

    central_command = docker_common_commands + ['-p', '127.0.0.1:%s:8000' % central_port, '-d', '-name', 'central', 'kalite:central']
    subprocess.call(central_command)
    central_info = json.loads(subprocess.check_output(['docker', 'inspect', 'central']).decode('utf-8'))

    dist_command = docker_common_commands + ['-p', '127.0.0.1:%s:8000' % dist_port, '-link', 'central:central', '-name', 'dev', 'kalite:dev']
    subprocess.call(dist_command)
    dist_info = json.loads(subprocess.check_output(['docker', 'inspect', 'dev']).decode('utf-8'))

    # the IDs we need
    central_id = central_info[0]['ID']
    dist_id = dist_info[0]['ID']

    # ok we're done, cleanup the containers
    print('cleaning up containers')
    subprocess.call(['docker', 'stop', '-t=3', central_id], stdout=subprocess.DEVNULL)
    subprocess.call(['docker', 'rm', central_id])

    subprocess.call(['docker', 'stop', '-t=3', dist_id], stdout=subprocess.DEVNULL)
    subprocess.call(['docker', 'rm', dist_id])
