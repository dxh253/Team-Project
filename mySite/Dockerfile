#FROM python:3.7.16

#ENV PYTHONUNBUFFERED=1

#WORKDIR .

#COPY .. .

#RUN pip install -r requirements.txt

#CMD sudo service postgresql start & python mysite/manage.py makemigrations & python mysite/manage.py migrate & python mysite/manage.py runserver 0.0.0.0:8000


#EXPOSE 8000


#FROM python:3.7.16

#ENV PYTHONUNBUFFERED=1

#RUN apt-get update && \
#    apt-get install -y postgresql && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*

#WORKDIR /app

#COPY . .

#RUN pip install -r requirements.txt

# add command to start PostgreSQL server
#CMD service postgresql start && \
#    python mysite/manage.py makemigrations && \
#    python mysite/manage.py migrate && \
#    python mysite/manage.py runserver 0.0.0.0:8000

#EXPOSE 8000

FROM python:3.7.16

ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y curl gnupg2 && \
    curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" | tee /etc/apt/sources.list.d/pgdg.list && \
    apt-get update && \
    apt-get install -y postgresql-14 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# add command to start PostgreSQL server
CMD service postgresql start && \
    python mysite/manage.py makemigrations && \
    python mysite/manage.py migrate && \
    python mysite/manage.py runserver 0.0.0.0:8000

EXPOSE 8000



