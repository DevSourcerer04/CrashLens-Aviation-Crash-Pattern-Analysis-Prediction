from src.aviation_crash.data_ingestion import DataIngestion
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

class DataIngestionTrainingPipeline:
    def main(self):
        ingestion = DataIngestion(
            raw_data_path="data/aviation_data.csv",
            output_path="artifacts/cleaned_data.csv"
        )
        ingestion.run()
