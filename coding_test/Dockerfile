## DockerFile to Build Image ##
FROM python:3.8-alpine3.10
LABEL maintainer tech.banerg@gmail.com

ENV HOME /root
ENV SERVE_PORT 5000

WORKDIR $HOME
ADD application $HOME/application
RUN chmod 755 -R $HOME/application &&\
    pip install -r application/requirements.txt
EXPOSE ${SERVE_PORT}
CMD [ "python", "/root/application/app.py" ]
