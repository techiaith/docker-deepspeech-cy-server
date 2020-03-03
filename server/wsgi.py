#!/usr/bin/env python3
import os
import sys
import glob
import wave
import cherrypy
import numpy as np

from packaging import version
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
        cherrypy.log("Loading DeepSpeech model....")

        self.deepspeech_version=os.environ["DEEPSPEECH_VERSION"]
        self.model_name=os.environ["MODEL_NAME"]
        self.model_version=os.environ["MODEL_VERSION"]

        if version.parse(self.deepspeech_version) < version.parse("0.6.0"):
            self.ds = Model(output_graph, N_FEATURES, N_CONTEXT, alphabet, BEAM_WIDTH)
            self.ds.enableDecoderWithLM(alphabet, lm, trie, LM_ALPHA, LM_BETA)
        else:
            self.ds = Model(output_graph, BEAM_WIDTH)
            self.ds.enableDecoderWithLM(lm, trie, LM_ALPHA, LM_BETA)

        cherrypy.log("Loading DeepSpeech model completed")


    @cherrypy.expose
    def index(self):
        msg = "<h1>DeepSpeech Server</h1>\n"
        return msg 


    @cherrypy.expose
    @cherrypy.tools.json_out(handler=callback_handler)
    def versions(self):
        result = {
            'version': 1,
            'deepspeech': self.deepspeech_version,
            'model_name': self.model_name,
            'model_version': self.model_version 
        }
        return result


    @cherrypy.expose
    @cherrypy.tools.json_out(handler=callback_handler)
    def speech_to_text(self, soundfile, **kwargs):
        upload_tmp_filepath = os.path.join(self.tmp_dir, 'ds_request_' + datetime.now().strftime('%y-%m-%d_%H%M%S') + '.wav')
        with open(upload_tmp_filepath, 'wb') as wavfile:
            while True:
                data = soundfile.file.read(8192)
                if not data:
                    break
                wavfile.write(data)

        result = {
                'version':1
        }

        #
        success = True
        fin = wave.open(upload_tmp_filepath, 'rb')
        fs = fin.getframerate()
        if fs != 16000:
            success = False

        audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)
        fin.close()

        text = self.ds.stt(audio)
        if len(text)==0:
            success=False

        result.update({
            'text': text,
            'success': success
        })

        return result



def resolve_models(dirName):
    pb = glob.glob(dirName + "/*.pb")[0]
    cherrypy.log("model file found: %s" % pb)

    alphabet = glob.glob(dirName + "/alphabet.txt")[0]
    cherrypy.log("model file found: %s" % alphabet)
    
    lm = glob.glob(dirName + "/lm.binary")[0]
    cherrypy.log("model file found: %s" % lm)
    
    trie = glob.glob(dirName + "/trie")[0]
    cherrypy.log("model file found: %s" % trie)

    return pb, alphabet, lm, trie



cherrypy.config.update({
    'environment': 'production',
    'log.screen': False,
    'response.stream': True,
    'log.access_file': 'deepspeech-access.log',
    'log.error_file': 'deepspeech-error.log',
})

cherrypy.tree.mount(DeepSpeechAPI(), '/')
application = cherrypy.tree

