FROM python:3.6
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN apt update
RUN apt install gettext -y
RUN pip install -r requirements.txt
ADD . /code/
