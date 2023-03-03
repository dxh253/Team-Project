FROM python:3.7.16

ENV PYTHONUNBUFFERED=1

WORKDIR .

COPY .. .

RUN pip install -r requirements.txt

CMD python manage.py makemigrations & python manage.py migrate & python manage.py runserver 13.42.48.103:8000


EXPOSE 8000

