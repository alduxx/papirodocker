FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
# RUN apt update && apt install -y gettext
RUN pip install -r requirements.txt
ADD . /code/
