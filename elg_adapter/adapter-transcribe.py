import traceback

from loguru import logger

from elg import QuartService
from elg.model import TextsResponse
from elg.quart_service import ProcessingError


class Adapter(QuartService):
    
    async def process_audio(self, content):
        try:
            # Make the remote call
            async with self.session.post("https://api.techiaith.org/deepspeech/transcribe/speech_to_text/", data={"soundfile": content.content}) as client_response:
                status_code = client_response.status
                content = await client_response.json()
        except:
            traceback.print_exc()
            raise ProcessingError.InternalError('Error calling API')

        if status_code >= 400:
            # if your API returns sensible error messages you could include that
            # instead of the generic message
            raise ProcessingError.InternalError('Error calling API')
        
        logger.info("Return the text response")
        return TextsResponse(texts=[{"content": content["text"]}])

service = Adapter("Adapter")
app = service.app
