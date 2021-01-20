FROM python:3.8

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2
#RUN apk update \
#    && apk add --virtual build-deps gcc python3-dev musl-dev \
#    && apk add postgresql-dev \
#    && pip install psycopg2 \
#    && apk del build-deps
#RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing gdal-dev
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin python-gdal python3-gdal
# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser myuser
USER myuser

# run gunicorn
CMD gunicorn musicevents.wsgi:application --bind 0.0.0.0:$PORT