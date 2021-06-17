from elg import FlaskService
from elg.model import TextsResponse

import requests

class Adapter(FlaskService):

    def process_audio(self, content):
        response = requests.post("https://api.techiaith.org/deepspeech/transcribe/speech_to_text/", files={"soundfile": content.content})
        assert response.ok, response.content     
        return TextsResponse(texts=[{"content": response.json()["text"]}])

flask_service = Adapter("Adapter")
app = flask_service.app
