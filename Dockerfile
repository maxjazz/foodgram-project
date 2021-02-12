FROM python:3.8.5

WORKDIR /code

COPY foodgram .

RUN pip install -r /code/requirements.txt

CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8080
