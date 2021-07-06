FROM python:3

RUN \
	apt-get install -y \
	wget \
	unzip \
	git

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg

RUN pip3 install numpy
RUN pip3 install opencv-python
RUN pip3 install requests
RUN pip3 install numba
RUN pip3 install imutils
RUN pip3 install requests

WORKDIR home/

COPY detect.py /home/
COPY object_scene.jpg /home/

RUN git clone https://github.com/pjreddie/darknet
WORKDIR darknet/

RUN wget https://pjreddie.com/media/files/yolov3.weights -P weights/
WORKDIR /home
