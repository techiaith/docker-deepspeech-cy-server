from elg import Service

service = Service.from_docker_image("techiaith/elg-adapter-deepspeech-server-cy-mascen", "http://localhost:8000/process", 8000)
result = service("question.mp3", "audio", sync_mode=True) # be sure to have the speech.mp3 file where you are running python
print(result)
