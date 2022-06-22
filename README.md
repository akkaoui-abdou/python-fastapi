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

<code>
    FROM python:3.10

    WORKDIR /fastapi-app

    COPY requirements.txt .

    RUN pip install -r requirements.txt

    COPY ./app ./app

    CMD [ "python3", "./app/main.py" ]
</code>




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