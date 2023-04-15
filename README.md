Docker Tutorial For Beginners - How To Containerize Python Applications
===
Create a simple project python API with action :
<ul>

<li>Create folder python-fastapi</li>
<li>Create virtual environment python </li>
<li>Generate file requierements.txt</li>
<li>Create file Dockerfile </li>
<li>Install requirements tools</li>
<li>build image docker</li>
</ul>


tree folder project
---

```bash

├── app
│   └── main.py
├── Dockerfile
├── README.md
└── requirements.txt

```

Create folder python-fastapi
---

```bash
mkdir python-fastapi
```

Create folder app for application
---

```bash
mkdir app
```

Create virtual environment python
---

```bash
python3 -m venv venv

source venv/bin/activate
```

Generate file requirements.txt
---

```bash
pip freeze > requirements.txt
```

Create file main.py for source code application
---

```bash
touch main.py
```

```python

from typing import Union

from fastapi import FastAPI

import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
   return ("Salut tout le monde")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")

```


Create file Dockerfile
---

```bash
touch Dockerfile
```


       FROM python:3.10

       WORKDIR /fastapi-app

       COPY requirements.txt .

       RUN pip install -r requirements.txt

       COPY ./app ./app

       CMD [ "python3", "./app/main.py" ]




build image docker
---

```bash
docker build -t fastapi-app .
```


Running with Docker
---

```bash
docker run -p 8000:8000 fastapi-app
```


interaction with container
---

```bash
docker exec -it id_contanier /bin/sh
```

Deployer this app with Google Kubernetes Engine: Create GKE Cluster
=========

```bash
export PROJECT_ID=kubernetes-366320
```

```bash
git clone https://github.com/akkaoui-abdou/python-fastapi.git
```
```bash
docker build -t us.gcr.io/${PROJECT_ID}/fastapi-app:v1 .
```
```bash
docker push us.gcr.io/${PROJECT_ID}/fastapi-app:v1
```

```bash
gcloud services enable containerregistry.googleapis.com
```
```bash
gcloud auth configure-docker
```


Create cluster:

```bash
gcloud config set compute/zone us-central1-a
```

```bash
gcloud container clusters create fastapi-cluster --num-nodes=1
```

```bash
gcloud container clusters get-credentials fastapi-cluster
```


Deployment application:

```bash
kubectl create deployment fastapi-app --image=us.gcr.io/${PROJECT_ID}/fastapi-app:v1 
```

```bash
kubectl expose deployment fastapi-app --type LoadBalancer --port 8000 --target-port 8000
```

```bash
kubectl get service
```
