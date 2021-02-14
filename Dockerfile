FROM python:3.9-slim

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        libatlas-base-dev gfortran nginx supervisor

RUN pip install uwsgi

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

RUN useradd --no-create-home nginx
RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache

COPY server-conf/nginx.conf /etc/nginx/
COPY server-conf/app-nginx.conf /etc/nginx/conf.d/default.conf
COPY server-conf/uwsgi.ini /etc/uwsgi/
COPY server-conf/supervisord.conf /etc/supervisor/

COPY . /app
WORKDIR /app
CMD ["/usr/bin/supervisord"]
