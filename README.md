# Python production ready API in Flask

- Flask
- Prometheus
- Docker
- UWSGI
- NGINX
- config and profiles

## Web in Python

WSGI, CGI, FastCGI etc. are all protocols for a web server to run code, and deliver the dynamic content that is produced.

CGI, FastCGI and SCGI are language agnostic. You can write CGI scripts in Perl, Python, C, bash, whatever. CGI defines which executable will be called, based on the URL, and how it will be called: the arguments and environment.

WSGI is Python only.

## Flask and uWSGI

Flask has a built-in web server, it’s not suitable for production and needs to be put behind a real web server to communicate with Flask through a WSGI protocol.
Gunicorn, uWSGI, etc. are widely used WSGI containers.  

Never expose a socket speaking the uwsgi protocol to the public network unless you know what you are doing. 
That channel allows for dynamic loading of applications (read: arbitrary execution of code). The protocol is meant to be sanitized/validated by a proxy like nginx, apache, the uWSGI routers…


## Important Commands

1. Start uwsgi application server on port 8085
   ```shell
   uwsgi --http 127.0.0.1:8085 --wsgi-file main.py --callable app 
   ```

2. Docker build and run the project.
   ```shell
   docker build -t flaskapp .
   docker run -p 8085:80 -it flaskapp:latest
   ```

3. Format the project python files using `autopep8`
   ```shell
   autopep8 --recursive --aggressive --aggressive --exclude="./myenv/*" --diff .     # view changes
   autopep8 --recursive --aggressive --aggressive --exclude="./myenv/*" --in-place . # format
   ```

## Important links for deploying Flask application

[Link 1](https://smirnov-am.github.io/running-flask-in-production-with-docker/)
 
[Link 2](https://medium.com/@gabimelo/developing-a-flask-api-in-a-docker-container-with-uwsgi-and-nginx-e089e43ed90e)


## DOs and DON'Ts

1. Though python is not a type-safe language, it pays well to have type safety. Various part of this project like route and config read from yaml provides type safety. 


2. A well behaved Python WSGI application should never attempt to write any data directly to sys.stdout or use the print statement without directing it to an alternate file object. 
   This is because ways of hosting WSGI applications such as CGI use standard output as the mechanism for sending the content of a response back to the web server. 
   If a WSGI application were to directly write to sys.stdout it could interfere with the operation of the WSGI adapter and result in corruption of the output stream.
