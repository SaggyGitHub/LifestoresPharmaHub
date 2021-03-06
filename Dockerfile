# syntax=docker/dockerfile:1

# pull the official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt 
#RUN python /life_pharma_project/manage.py loaddata pharmaceuticals.json

# copy project
COPY . /usr/src/app

EXPOSE 8000


#CMD ["python", "life_pharma_project/manage.py", "loaddata", "life_pharma_project/lifepharma/fixtures/pharmaceuticals.json"]
CMD ["python", "life_pharma_project/manage.py", "runserver", "0.0.0.0:8000"]

