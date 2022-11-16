from pymongo import mongo_client
import pymongo
from app.config import settings
import logging


"""
client = mongo_client.MongoClient(settings.MONGO_URL)
print('Connected to MongoDB...')

db = client[settings.MONGO_DB]
User = db.users
Post = db.posts
User.create_index([("email", pymongo.ASCENDING)], unique=True)
Post.create_index([("title", pymongo.ASCENDING)], unique=True)
"""

def db_get_db():
    try:
        connection = mongo_client.MongoClient(settings.MONGO_URL)
        db = connection[settings.MONGO_DB]
        return db
    except pymongo.errors.ConnectionFailure as e:
        logging.info("database connection failure: {}".format(str(e)))


def get_collection_mongodb(collection):
    try:
        db = db_get_db()
        mycol = db[collection]
        return mycol
    except Exception as e:
        logging.info("database connection failure: {}".format(str(e)))

def db_create_job(job):
    jobs_collection = get_collection_mongodb("jobs")
    job_dict = {
        "job_id": job['job_id'], 
        "web_url": job['web_url'], 
        "create_date": job['create_date'], 
        "update_date": job['update_date'],
        "status": job['status'],
        "execution_id": job['execution_id'],
        "ressource": job['ressource'],
        "service_id": job['service_id'],
        "operation": job['operation'],
        "client_basicat": job['client_basicat']
    }
    result_col_job = jobs_collection.insert_one(job_dict)
    return result_col_job