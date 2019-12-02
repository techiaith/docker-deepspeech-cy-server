#!/usr/bin/env python3
import os
import sys
import glob

import cherrypy

from datetime import datetime
from deepspeech import Model

from handlers import callback_handler


# DeepSpeech config..
DEEPSPEECH_MODEL_DIR='/deepspeech/models'

N_FEATURES = 26
N_CONTEXT = 9
BEAM_WIDTH = 500
LM_ALPHA = 0.75
LM_BETA = 1.85



class DeepSpeechAPI(object):


    def __init__(self):
        self.tmp_dir = '/tmp'

        output_graph, alphabet, lm, trie = resolve_models(DEEPSPEECH_MODEL_DIR)

        self.ds = Model(output_graph, N_FEATURES, N_CONTEXT, alphabet, BEAM_WIDTH)
        self.ds.enableDecoderWithLM(alphabet, lm, trie, LM_ALPHA, LM_BETA)


    @cherrypy.expose
    def index(self):
        msg = "<h1>DeepSpeech Server</h1>\n"
        return msg 


    @cherrypy.expose
    @cherrypy.tools.json_out(handler=callback_handler)
    def speech_to_text(self, soundfile, **kwargs):
        upload_tmp_filepath = os.path.join(self.tmp_dir, 'ds_request_' + datetime.now().strftime('%y-%m-%d_%H%M%S'))
        with open(upload_tmp_filepath, 'wb') as wavfile:
            while True:
                data = soundfile.file.read(8192)
                if not data:
                    break
                wavfile.write(data)

        result = {
                'version':1
        }
        result.update({'text': self.ds.stt(upload_tmp_filepath, 16000)})
        return result



def resolve_models(dirName):
    pb = glob.glob(dirName + "/*.pb")[0]
    alphabet = glob.glob(dirName + "/alphabet.txt")[0]
    lm = glob.glob(dirName + "/lm.binary")[0]
    trie = glob.glob(dirName + "/trie")[0]

    return pb, alphabet, lm, trie


cherrypy.config.update({
    'environment': 'production',
    'log.screen': False,
    'response.stream': True,
    'log.error_file': 'deepspeech-server.log',
})

cherrypy.tree.mount(DeepSpeechAPI(), '/')
application = cherrypy.tree

