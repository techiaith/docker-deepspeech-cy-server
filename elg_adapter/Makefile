default: build

version:
	$(eval MODEL_VERSION = 0.2)

macsen-config:
	cp ../question.* .
	cp adapter-macsen.py adapter.py
	$(eval MODEL_NAME = macsen)

transcribe-config:
	cp ../speech.* .
	cp adapter-transcribe.py adapter.py
	$(eval MODEL_NAME = transcribe)


build-macsen: version macsen-config build-model
build-transcribe: version transcribe-config build-model

run-macsen: version macsen-config run-model
run-transcribe: version transcribe-config run-model

stop-macsen: macsen-config stop-model
stop-transcribe: transcribe-config stop-model

clean-macsen: version macsen-config clean-model
clean-transcribe: version transcribe-config clean-model

publish-macsen: version macsen-config publish-model
publish-transcribe: version transcribe-config publish-model

build:
	echo "Missing model name. e.g. make build-transcribe "


build-model:
	elg docker create --path ./adapter.py --classname Adapter --service_type quart
	docker build -t techiaith/elg-adapter-deepspeech-server-cy-${MODEL_NAME}:${MODEL_VERSION} .


run-model:
	docker run --name elg-adapter-deepspeech-server-cy-${MODEL_NAME} \
	    --network host \
	    -d -p 8000:8000 \
	    techiaith/elg-adapter-deepspeech-server-cy-${MODEL_NAME}:${MODEL_VERSION}


publish-model:
	docker push techiaith/elg-adapter-deepspeech-server-cy-${MODEL_NAME}:${MODEL_VERSION}


stop-model:
	-docker stop elg-adapter-deepspeech-server-cy-${MODEL_NAME}
	-docker rm elg-adapter-deepspeech-server-cy-${MODEL_NAME}


clean-model:
	-docker rmi techiaith/elg-adapter-deepspeech-server-cy-${MODEL_NAME}:${MODEL_VERSION}

