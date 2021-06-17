default: build

macsen-config:
	cp ../question.wav .
	cp adapter-macsen.py adapter.py
	$(eval MODEL_NAME = macsen)

transcribe-config:
	cp ../speech.wav .
	cp adapter-transcribe.py adapter.py
	$(eval MODEL_NAME = transcribe)


build-macsen: macsen-config build-model
build-transcribe: transcribe-config build-model

run-macsen: macsen-config run-model
run-transcribe: transcribe-config run-model

stop-macsen: macsen-config stop-model
stop-transcribe: transcribe-config stop-model

clean-macsen: macsen-config clean-model
clean-transcribe: transcribe-config clean-model

publish-macsen: macsen-config publish-model
publish-transcribe: transcribe-config publish-model


build:
	echo "Missing model name. e.g. make build-transcribe "


build-model:
	elg docker create --path ./adapter.py --classname Adapter
	docker build -t techiaith/elg-adapter-deepspeech-server-cy-${MODEL_NAME} .


run-model:
	docker run --name elg-adapter-deepspeech-server-cy-${MODEL_NAME} \
	    --network host \
	    -d -p 8000:8000 \
	    techiaith/elg-adapter-deepspeech-server-cy-${MODEL_NAME}


publish-model:
	docker push techiaith/elg-adapter-deepspeech-server-cy-${MODEL_NAME}


stop-model:
	-docker stop elg-adapter-deepspeech-server-cy-${MODEL_NAME}
	-docker rm elg-adapter-deepspeech-server-cy-${MODEL_NAME}


clean-model:
	-docker rmi techiaith/elg-adapter-deepspeech-server-cy-${MODEL_NAME}


