FROM python:3.7.16

ENV PYTHONUNBUFFERED=1

WORKDIR .

COPY .. .

RUN pip install -r requirements.txt

CMD python mySite/mysite/manage.py makemigrations & python mySite/mysite/manage.py migrate & python mySite/mysite/manage.py runserver 0.0.0.0:8000


EXPOSE 8000

