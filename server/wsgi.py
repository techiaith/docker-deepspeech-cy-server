#!/usr/bin/env python3
import os
import sys
import glob
import wave
import cherrypy
import numpy as np

import eyed3
from pydub import AudioSegment

from packaging import version
from datetime import datetime
from deepspeech import Model

from handlers import callback_handler


# DeepSpeech config..
DEEPSPEECH_MODEL_DIR='/deepspeech/models'

STATIC_PATH=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static_html')
class StaticRoot(object): pass

class DeepSpeechAPI(object):


    def __init__(self):
        self.tmp_dir = '/recordings'

        self.deepspeech_version=os.environ["DEEPSPEECH_VERSION"]
        self.model_name=os.environ["MODEL_NAME"]
        self.model_version=os.environ["MODEL_VERSION"]

        acoustic_model, language_model = self.resolve_models(DEEPSPEECH_MODEL_DIR)
        cherrypy.log("Loading DeepSpeech model....")

        self.ds = Model(acoustic_model)
        self.ds.enableExternalScorer(language_model)

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
        upload_tmp_filepath = os.path.join(self.tmp_dir, 'ds_request_' + datetime.now().strftime('%y-%m-%d_%H%M%S') + '.raw')
        with open(upload_tmp_filepath, 'wb') as wavfile:
            while True:
                data = soundfile.file.read(8192)
                if not data:
                    break
                wavfile.write(data)

        cherrypy.log("tmp file written to %s" % upload_tmp_filepath)

        result = {
                'version':1
        }

        #
        success = False
        text = ''

        upload_filepath = self.resolve_audio_format(upload_tmp_filepath)

        if len(upload_filepath)>0:
            success=True
            cherrypy.log("Starting STT ....")
            fin = wave.open(upload_filepath, 'rb')
            audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)
            fin.close()

            text = self.ds.stt(audio)

            if len(text)==0:
                cherrypy.log("STT not a success")
                success=False
            else:
                cherrypy.log("STT successful")


        result.update({
            'text': text,
            'success': success
        })

        return result



    def resolve_audio_format(self, upload_raw_filepath):
        upload_filepath = upload_raw_filepath
        mp3_audio=eyed3.load(upload_raw_filepath)
        if mp3_audio!=None:
            upload_filepath = upload_raw_filepath.replace(".raw", ".mp3") 
            os.rename(upload_raw_filepath, upload_filepath)

            sound = AudioSegment.from_mp3(upload_filepath)
            sound = sound.set_frame_rate(16000)
            sound = sound.set_channels(1)
            sound.export(upload_filepath.replace(".mp3", ".wav"), format="wav")

            upload_filepath = upload_filepath.replace(".mp3", ".wav")
        else:
            upload_filepath = upload_raw_filepath.replace(".raw",".wav") 
            os.rename(upload_raw_filepath, upload_filepath)

        fin = wave.open(upload_filepath, 'rb')
        fs = fin.getframerate()
        if fs != 16000:
            return ''

        return upload_filepath



    def resolve_models(self, dirName):
        pb_wildcard = "/*_%s.pbmm" % self.model_version
        pb = glob.glob(dirName + pb_wildcard)[0]
        cherrypy.log("model file found: %s" % pb)

        scorer_wildcard = "/*_%s_%s.scorer" % (self.model_name, self.model_version)
        scorer = glob.glob(dirName + scorer_wildcard)[0]
        cherrypy.log("scorer model file found: %s" % scorer)
    
        return pb, scorer


cherrypy.config.update({
    'environment': 'production',
    'log.screen': False,
    'response.stream': True,
    'log.access_file': '/var/log/deepspeech-server/deepspeech-access.log',
    'log.error_file': '/var/log/deepspeech-server/deepspeech-error.log',
})


cherrypy.tree.mount(StaticRoot(), '/static', config={
    '/': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': STATIC_PATH,
        'tools.staticdir.index': 'index.html',
         },
    })


cherrypy.tree.mount(DeepSpeechAPI(), '/')
application = cherrypy.tree

