#!/bin/bash
echo "Starting CherryPy..."
supervisord -c /deepspeech/server/cherrypy.conf
sleep infinity
