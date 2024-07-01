from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import logging

logger = logging.getLogger('logger')

# Replace the placeholder with your Atlas connection string
uri = "mongodb://localhost:27017"


# Send a ping to confirm a successful connection
def store(db_name, collection_name, record):
    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client[db_name]
        collection = db[collection_name]
        record_id = collection.insert_one(record).inserted_id
    except Exception as ex:
        logger.info("Error storing the task: " + str(ex) + "...")
        record_id = None
    return record_id


def check_record(db_name, collection_name, query):
    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client[db_name]
        collection = db[collection_name]
        record = collection.find_one(query)
        if record is not None:
            return True
        else:
            return False
    except Exception as ex:
        logger.info("Error checking the record: " + str(ex) + "...")
        return False


def retrieve_records(db_name, collection_name, query):
    retrieved_records = []
    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client[db_name]
        collection = db[collection_name]
        records = collection.find(query)
        for record in records:
            retrieved_records.append(record)
    except Exception as ex:
        logger.debug("Error retrieving the records: " + str(ex) + "...")
        retrieved_records = {}
    return retrieved_records
