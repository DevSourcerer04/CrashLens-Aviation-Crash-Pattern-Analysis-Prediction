import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

class DataCleaning:
    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

    def load_data(self):
        logging.info(f"Loading data from {self.input_path}")
        return pd.read_csv(self.input_path)

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info("Starting data cleaning process...")

        # Drop duplicates
        df.drop_duplicates(inplace=True)

        # Drop rows with too many nulls (threshold can be adjusted)
        df.dropna(thresh=len(df.columns) - 3, inplace=True)

        # Convert date column if present
        for col in df.columns:
            if "date" in col.lower():
                try:
                    df[col] = pd.to_datetime(df[col], errors='coerce')
                except:
                    logging.warning(f"Could not convert column '{col}' to datetime.")

        # Strip whitespace from column names
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        logging.info(f"Cleaned data shape: {df.shape}")
        return df

    def save_data(self, df: pd.DataFrame):
        df.to_csv(self.output_path, index=False)
        logging.info(f"Saved cleaned data to {self.output_path}")

    def run(self):
        df = self.load_data()
        cleaned_df = self.clean_data(df)
        self.save_data(cleaned_df)
