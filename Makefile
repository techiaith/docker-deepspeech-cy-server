
# --- Runtime with Python REST API  ----------------------------------------------------

macsen-config:
	$(eval DEEPSPEECH_VERSION = 0.5.1)
	$(eval MODEL_NAME = macsen)
	$(eval MODEL_VERSION= 200309)
	$(eval PORT_NUMBER = 5503)

transcribe-config:
	$(eval DEEPSPEECH_VERSION = 0.7.4)
	$(eval MODEL_NAME = transcribe)
	$(eval MODEL_VERSION = 20.06)
	$(eval PORT_NUMBER = 5501)

build-macsen: macsen-config build
run-macsen: macsen-config run
stop-macsen: macsen-config stop
clean-macsen: macsen-config stop clean

build-transcribe: transcribe-config build
run-transcribe: transcribe-config run
stop-transcribe: transcribe-config stop
clean-transcribe: transcribe-config stop clean

build: 
	docker build --rm -t techiaith/deepspeech-${DEEPSPEECH_VERSION}-server \
		--build-arg DEEPSPEECH_VERSION=${DEEPSPEECH_VERSION} \
		--build-arg MODEL_NAME=${MODEL_NAME} \
		--build-arg MODEL_VERSION=${MODEL_VERSION} \
		.

run:
	if [ ! -d "models/${MODEL_NAME}" ]; then \
            mkdir -p models/${MODEL_NAME}; \
            cd models/${MODEL_NAME} && \
	    wget -O - https://github.com/techiaith/docker-deepspeech-cy/releases/download/${MODEL_VERSION}/techiaith_bangor_${MODEL_VERSION}.pbmm;\
	    wget -O - https://github.com/techiaith/docker-deepspeech-cy/releases/download/${MODEL_VERSION}/techiaith_bangor_${MODEL_NAME}_${MODEL_VERSION}.scorer;\
        fi
	docker run --name deepspeech-server-${MODEL_NAME} --restart=always \
		-it -d -p ${PORT_NUMBER}:8008  \
		-v ${PWD}/models/${MODEL_NAME}:/deepspeech/models \
		techiaith/deepspeech-${DEEPSPEECH_VERSION}-server

stop:
	-docker stop deepspeech-server-${MODEL_NAME}
	-docker rm deepspeech-server-${MODEL_NAME}

clean:
	docker rmi techiaith/deepspeech-${DEEPSPEECH_VERSION}-server

