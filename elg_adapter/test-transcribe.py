from elg import Service

service = Service.from_docker_image("techiaith/elg-adapter-deepspeech-server-cy-transcribe", "http://localhost:8000/process", 8000)
result = service("speech.wav", "audio", sync_mode=True) # be sure to have the speech.wav file where you are running python
print(result)
