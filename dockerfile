FROM python:3.11

ADD . /usr/hackernewstm

WORKDIR /usr/hackernewstm

COPY . .

RUN pip install -U setuptools && pip install -U -r requirements.txt

EXPOSE 8000

CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]
