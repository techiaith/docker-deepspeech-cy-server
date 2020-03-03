
# --- Runtime with Python REST API  ----------------------------------------------------

macsen-config:
	DEEPSPEECH_VERSION=0.6.1
	MODEL_NAME=macsen
	MODEL_VERSION=200121
	PORT_NUMBER=5500

arddweud-config:
	DEEPSPEECH_VERSION=0.5.1
	MODEL_NAME=arddweud
	MODEL_VERSION=200303
	PORT_NUMBER=5501

build-macsen: macsen-config build
run-macsen: macsen-config run
stop-macsen: macsen-config stop

run-arddweud: arddweud-config run
stop-arddweud: arddweud-config stop

build: 
	docker build --rm -t techiaith/deepspeech-${DEEPSPEECH_VERSION}-server \
		--build-arg DEEPSPEECH_VERSION=${DEEPSPEECH_VERSION} \
		--build-arg MODEL_NAME=${MODEL_NAME} \
		--build-arg MODEL_VERSION=${MODEL_VERSION} \
		.

run:
	if [ ! -d "models/${MODEL_NAME}" ]; then \
            mkdir -p models/macsen; \
            cd models/macsen; && \
	    wget -O - http://techiaith.cymru/deepspeech/${MODEL_NAME}/models/${DEEPSPEECH_VERSION}/${MODEL_NAME}_${MODEL_VERSION}.tar.gz | tar xvfz -;\
        fi
	docker run --name deepspeech-server-${MODEL_NAME} --restart=always \
		-it -d -p ${PORT_NUMBER}:8008  \
		-v ${PWD}/models/${MODEL_NAME}:/deepspeech/models
		techiaith/deepspeech-server 


stop:
	docker stop deepspeech-server-${MODEL_NAME}
	docker rm deepspeech-server-${MODEL_NAME}


clean:
	docker rmi techiaith/deepspeech-server

