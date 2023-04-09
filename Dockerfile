FROM python:3.10

ENV CONTAINER_HOME=/usr/src/app

RUN mkdir -p $CONTAINER_HOME

WORKDIR $CONTAINER_HOME

COPY requirements.txt $CONTAINER_HOME

RUN pip install -r $CONTAINER_HOME/requirements.txt

COPY ./app $CONTAINER_HOME

CMD [ "python3", "main.py" ]
