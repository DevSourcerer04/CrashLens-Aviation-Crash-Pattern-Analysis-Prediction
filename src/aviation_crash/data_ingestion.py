import os
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

class DataIngestion:
    def __init__(self, raw_data_path: str, output_path: str):
        self.raw_data_path = raw_data_path
        self.output_path = output_path
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

    def load_data(self) -> pd.DataFrame:
        logging.info(f"Reading raw dataset from: {self.raw_data_path}")
        df = pd.read_csv(self.raw_data_path)
        logging.info(f"Loaded dataset shape: {df.shape}")
        return df

    def save_data(self, df: pd.DataFrame) -> None:
        df.to_csv(self.output_path, index=False)
        logging.info(f"Saved processed data to: {self.output_path}")

    def run(self):
        df = self.load_data()
        # Optionally, add basic cleaning here or leave it for a separate module
        self.save_data(df)

