FROM python:3.11

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -

RUN apt-get install -y nodejs

COPY . .

WORKDIR /reservation-app

RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh
