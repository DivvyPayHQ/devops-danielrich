# Docker file for a CentOS-based Python3 image
# Main contents taken from https://hub.docker.com/r/fnndsc/centos-python3/~/dockerfile/
FROM centos/s2i-base-centos7

ENV PYTHON_VERSION=3.6 \
    PATH=$HOME/.local/bin/:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    PIP_NO_CACHE_DIR=off

RUN yum install -y centos-release-scl-rh && \
    yum-config-manager --enable centos-sclo-rh-testing && \
    INSTALL_PKGS="rh-python36 rh-python36-python-pip" &&\
    yum install -y --setopt=tsflags=nodocs --enablerepo=centosplus $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    yum clean all -y

RUN source scl_source enable rh-python36 && \
    virtualenv /opt/app-root && \
    chown -R 1001:0 /opt/app-root && \
    fix-permissions /opt/app-root && \
    rpm-file-permissions


##### Added content for SWAPI image #####

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD chalice local --host=0.0.0.0 --port=80
