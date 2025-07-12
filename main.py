import sys
import os

from aviation_crash.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from aviation_crash.pipeline.stage_02_data_cleaning import DataCleaningTrainingPipeline


import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

### STAGE 1: Data Ingestion
STAGE_NAME = "Data Ingestion Stage"
try:
    logging.info(f"\n\n{'>'*10} {STAGE_NAME} started {'<'*10}\n")
    ingestion = DataIngestionTrainingPipeline()
    ingestion.main()
    logging.info(f"\n{'='*10} {STAGE_NAME} completed {'='*10}\n")
except Exception as e:
    logging.exception(e)
    raise e

### STAGE 2: Data Cleaning
STAGE_NAME = "Data Cleaning Stage"
try:
    logging.info(f"\n\n{'>'*10} {STAGE_NAME} started {'<'*10}\n")
    cleaner = DataCleaningTrainingPipeline()
    cleaner.main()
    logging.info(f"\n{'='*10} {STAGE_NAME} completed {'='*10}\n")
except Exception as e:
    logging.exception(e)
    raise e
