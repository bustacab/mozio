FROM python:3.7
LABEL maintainer="Santiago B <jsantiagobustamantee@gmail.com>"
LABEL editor="Santiago B <jsantiagobustamantee@gmail.com>"

ENV PYTHONUNBUFFERED 1


# Clean Install
RUN apt-get update && apt-get install -y python3-pip python-dev && apt-get clean
RUN pip install --upgrade pip

RUN apt-get install -y binutils libproj-dev gdal-bin

RUN pip install virtualenv

############################# Installing code
RUN mkdir /code
ADD requirements/common.txt /code/requirements/

WORKDIR /code

RUN pip install -r requirements/common.txt

CMD ["python", "manage.py", "migrate"]
EXPOSE 8000
