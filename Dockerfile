FROM ubuntu:16.04
MAINTAINER Uned Technolegau Iaith, Prifysgol Bangor University

RUN apt-get update \
 && apt-get install -y \
	git supervisor python3 python3-pip python3-dev \
        cmake wget curl locales vim zip zlib1g-dev \
        rabbitmq-server \
 && pip3 install --upgrade pip


# Set the locale
RUN locale-gen cy_GB.UTF-8
ENV LANG cy_GB.UTF-8  
ENV LANGUAGE cy_GB:en  
ENV LC_ALL cy_GB.UTF-8

#
RUN mkdir -p /deepspeech/server && mkdir -p /deepspeech/models && mkdir -p /deepspeech/data
COPY server/requirements.txt /deepspeech/server

WORKDIR /deepspeech/server 
RUN pip3 install -r requirements.txt

WORKDIR /deepspeech/models
RUN wget -O - http://techiaith.cymru/deepspeech/macsen/models/0.5.1/macsen.tar.gz | tar xvfz -

WORKDIR /deepspeech/data
RUN wget -O - http://techiaith.cymru/deepspeech/macsen/macsen_191126.tar.gz | tar xvfz -

EXPOSE 8008

#CMD ["/bin/bash", "-c", "/opt/skills-online-api/start.sh"]

