import os
import sys
import numpy as np  
import pandas as pd

"""
defining constants for training pipeline 
"""
TARGET_COLUMN = "Load Demand (kW)"
PIPELINE_NAME="LOAD_DEMAND"
ARTIFACT_DIR="Artifacts"
FILE_NAME="hourly_data.csv"
TRAIN_FILE_NAME="train.csv"
TEST_FILE_NAME="test.csv"



""" Data ingestion related constants"""

DATA_INGESTION_COLLECTION_NAME = "hourly_data"
DATA_INGESTION_DATABASE_NAME = "power_flow"
DATA_INGESTION_Directory_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2

