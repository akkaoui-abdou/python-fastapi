from typing import Union
from fastapi import FastAPI
import uvicorn
import logging
import datetime
import json
import uuid
import app.database as database

app = FastAPI()


logging.basicConfig(
filename=f"fss.log",
format="%(asctime)s %(name)s - %(levelname)s - %(message)s",
level=logging.INFO,
)




@app.get("/createjob")
def read_root():

    uuid_job = uuid.uuid4().hex


    job_dict = {
        "job_id": uuid_job, 
        "web_url": "", 
        "create_date": datetime.datetime.now(),
        "update_date": datetime.datetime.now(),
        "status": "created",
        "execution_id": "1222",
        "ressource": "",
        "service_id": "1222",
        "operation": "createjob",
        "client_basicat": "STK"
        }

    database.db_create_job(job_dict)
    logging.info("get results from the DB")
    return ("Salut tout le monde")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


"""
if __name__ == "__main__":
    uvicorn.run(app, port=8100, host="0.0.0.0")
"""