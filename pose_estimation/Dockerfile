FROM python:2

RUN \
	apt-get install -y \
	wget \
	unzip \
	git

RUN pip install Flask

WORKDIR home/

COPY app.py /home/

WORKDIR /home
