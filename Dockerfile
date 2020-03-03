FROM ubuntu:16.04
MAINTAINER Uned Technolegau Iaith, Prifysgol Bangor University


RUN apt-get update \
 && apt-get install -y \
	git supervisor python3 python3-pip python3-dev \
        cmake wget curl locales vim zip zlib1g-dev \
 && pip3 install --upgrade pip


# Set the locale
RUN locale-gen cy_GB.UTF-8
ENV LANG cy_GB.UTF-8  
ENV LANGUAGE cy_GB:en  
ENV LC_ALL cy_GB.UTF-8

#
RUN mkdir -p /deepspeech/server && mkdir -p /deepspeech/models

WORKDIR /deepspeech/server 
COPY server/ /deepspeech/server

ARG DEEPSPEECH_VERSION
ARG MODEL_NAME
ARG MODEL_VERSION

ENV DEEPSPEECH_VERSION=${DEEPSPEECH_VERSION}
ENV MODEL_NAME=${MODEL_NAME}
ENV MODEL_VERSION=${MODEL_VERSION}

RUN pip3 install deepspeech==$DEEPSPEECH_VERSION
RUN pip3 install -r requirements.txt

EXPOSE 8008

CMD ["/bin/bash", "-c", "/deepspeech/server/start.sh"]

