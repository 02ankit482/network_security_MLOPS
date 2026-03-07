import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

# certifi is a Python library that provides a collection of Root Certificates for validating the trustworthiness of SSL certificates while making HTTPS requests. It is commonly used in Python applications to ensure secure communication over the internet by verifying the authenticity of SSL certificates presented by servers.
# The certifi library is often used in conjunction with libraries like requests to ensure that HTTPS requests are made securely by validating the server's SSL certificate against a trusted set of root certificates. This helps
import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
from pymongo import MongoClient
from networksecurity.exception.exception import MyException
from networksecurity.logging.logger import logging  
from pathlib import Path

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except exception as e:
            raise MyException(e, sys)
        
    def csv_to_json(self, file_path: str) -> str:
        """
        Converts a CSV file to JSON format.

        :param file_path: The path to the CSV file.
        :return: A JSON string representation of the CSV data.
        """
        try:
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            records= list(json.loads(df.T.to_json()).values())
            return records
        except Exception as e:
            raise MyException(e, sys)
    def insert_data_mongodb(self, records, database, collection):
        """
        Inserts data into a MongoDB collection.

        :param records: The data to be inserted, typically a list of dictionaries.
        :param database: The name of the MongoDB database.
        :param collection: The name of the MongoDB collection.
        """
        try:
            client = MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            db = client[database]
            coll = db[collection]
            coll.insert_many(records)
            return len(records)
           
        except Exception as e:
            raise MyException(e, sys)
        

if __name__ == "__main__":
    FILE_PATH = Path(r"D:\MLOPS_2\network_security_MLOPS\Network_Data\hourly_data.csv")
    DATABASE = "power_flow" 
    COLLECTION = "hourly_data"
    NetworkDataExtract_obj = NetworkDataExtract()
    NetworkDataExtract_obj.csv_to_json(FILE_PATH)
    records= NetworkDataExtract_obj.csv_to_json(FILE_PATH)
    no_of_records = NetworkDataExtract_obj.insert_data_mongodb(records, DATABASE, COLLECTION)  
    print(f"{no_of_records} records inserted successfully into MongoDB collection '{COLLECTION}' in database '{DATABASE}'.")