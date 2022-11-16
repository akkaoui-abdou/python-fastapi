FROM python:3.10

WORKDIR /fastapi-app

COPY requirements.txt .

# Install pipenv
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY ./app ./app

#CMD [ "python3", "./app/main.py" ]