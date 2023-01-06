FROM python:3.10.4-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN apt-get install python2-dev -y
RUN apt-get install build-essential -y
RUN python3 -m pip install -U pip
RUN pip3 install --upgrade setuptools 
RUN pip3 install -U -r requirements.txt
RUN mkdir /YUI
WORKDIR /YUI
COPY . .
CMD ["python3" , "-m" , "YUI"]
