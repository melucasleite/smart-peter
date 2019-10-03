FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    python-pip \
    python-dev \
    build-essential \
    tzdata \
    locales \
    git

RUN echo "America/Bahia" >/etc/timezone && \
ln -sf /usr/share/zoneinfo/America/Bahia /etc/localtime && \
dpkg-reconfigure -f noninteractive tzdata
RUN echo 'pt_BR.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen && DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales

COPY requirements.txt /usr/src/app/

RUN pip install -r requirements.txt

COPY . /usr/src/app
EXPOSE 5000

#CMD ["gunicorn --bind 0.0.0.0:7000 wsgi:app -w 15"]
