

# --- Runtime with Python REST API  ----------------------------------------------------
build: 
	docker build --rm -t techiaith/deepspeech-server .

run: 
	docker run --name deepspeech-server --restart=always \
		-it -p 5500:8008  \
		-v ${PWD}/server:/deepspeech/server \
		techiaith/deepspeech-server bash

stop:
	docker stop deepspeech-server
	docker rm deepspeech-server

clean:
	docker rmi techiaith/deepspeech-server

