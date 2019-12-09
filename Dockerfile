FROM ubuntu:16.04
MAINTAINER Uned Technolegau Iaith, Prifysgol Bangor University

ENV DEEPSPEECH_VERSION=0.6.0

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
RUN mkdir -p /deepspeech/server && mkdir -p /deepspeech/models && mkdir -p /deepspeech/data

WORKDIR /deepspeech/models
RUN wget -O - http://techiaith.cymru/deepspeech/macsen/models/$DEEPSPEECH_VERSION/macsen.tar.gz | tar xvfz -

WORKDIR /deepspeech/data
RUN wget -O - http://techiaith.cymru/deepspeech/macsen/macsen_191126.tar.gz | tar xvfz -

WORKDIR /deepspeech/server 
COPY server/ /deepspeech/server

RUN pip3 install deepspeech==$DEEPSPEECH_VERSION
RUN pip3 install -r requirements.txt

EXPOSE 8008

CMD ["/bin/bash", "-c", "/deepspeech/server/start.sh"]

