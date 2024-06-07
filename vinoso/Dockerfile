# pull the official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# install dependencies
RUN python3 -m pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY /srv/vinoso/vinoso/ /usr/src/app
COPY /srv/vinoso/vinoso/static/ /usr/src/app/static

EXPOSE 8000
