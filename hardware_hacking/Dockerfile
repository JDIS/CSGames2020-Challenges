FROM debian:stretch-slim

RUN apt-get update && apt-get install -y build-essential procps strace

COPY dist /opt
COPY README.txt /root

RUN echo '/opt/start.sh || logout' >> ~/.bash_login
RUN echo 'cd ~' >> ~/.bashrc

ENTRYPOINT . /root/.bashrc && /bin/bash -l
