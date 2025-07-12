from src.aviation_crash.data_cleaning import DataCleaning
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

class DataCleaningTrainingPipeline:
    def main(self):
        cleaner = DataCleaning(
            input_path="artifacts/cleaned_data.csv",
            output_path="artifacts/final_data.csv"
        )
        cleaner.run()
