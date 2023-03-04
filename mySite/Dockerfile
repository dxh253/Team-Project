FROM python:3.7.16

ENV PYTHONUNBUFFERED=1

WORKDIR .

COPY .. .

RUN pip install -r requirements.txt

CMD python mysite/manage.py makemigrations & python mysite/manage.py migrate & python mysite/manage.py runserver 0.0.0.0:8000


EXPOSE 8000

