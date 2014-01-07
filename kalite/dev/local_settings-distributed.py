# NOTE: depends on a link between another central server container. Consult the setup_dev_environment.py script

import os

DEBUG = True

SECURESYNC_PROTOCOL = "http"
CENTRAL_SERVER_HOST = os.environ['CENTRAL_PORT_8000_TCP_ADDR'] + ':' +  os.environ['CENTRAL_PORT_8000_TCP_PORT']
