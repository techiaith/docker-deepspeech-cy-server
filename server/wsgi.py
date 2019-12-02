#!/usr/bin/env python3
import os
import sys

import cherrypy
import logging

#from .deepspeech.handlers import callback_handler


class DeepSpeechAPI(object):

    def __init__(self):
        self.tmp_dir = '/tmp'

    @cherrypy.expose
    def index(self):
        msg = "<h1>DeepSpeech Server</h1>\n"
        return msg 


cherrypy.config.update({
    'environment': 'production',
    'log.screen': False,
    'response.stream': True,
    'log.error_file': 'deepspeech-server.log',
})

cherrypy.tree.mount(DeepSpeechAPI(), '/')
application = cherrypy.tree

