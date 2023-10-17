FROM python:3.11

ENV DockerHOME=/home/apps/ztm_scrappers/

RUN mkdir -p $DockerHOME

RUN apt-get update -y -q
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential -y -q

WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ztm_scrappers $DockerHOME
RUN pip install -r requirements.txt


RUN chmod +x /home/apps/ztm_scrappers/start.sh
ENTRYPOINT ["./start.sh"]