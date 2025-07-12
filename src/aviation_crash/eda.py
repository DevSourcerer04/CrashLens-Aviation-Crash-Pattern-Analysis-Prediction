import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

class EDA:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.df = None

    def load_data(self):
        logging.info(f"Loading data from {self.data_path}")
        self.df = pd.read_csv(self.data_path)

    def missing_values_summary(self):
        nulls = self.df.isnull().sum()
        logging.info(f"Null values per column:\n{nulls[nulls > 0]}")
        return nulls

    def top_crash_causes(self, cause_column='cause', top_n=10):
        plt.figure(figsize=(10, 6))
        self.df[cause_column].value_counts().head(top_n).plot(kind='barh')
        plt.title(f"Top {top_n} Crash Causes")
        plt.xlabel("Count")
        plt.ylabel("Cause")
        plt.tight_layout()
        plt.show()

    def crashes_over_time(self, date_column='date'):
        df_time = self.df.copy()
        df_time[date_column] = pd.to_datetime(df_time[date_column], errors='coerce')
        df_time = df_time.dropna(subset=[date_column])
        df_time['year'] = df_time[date_column].dt.year
        plt.figure(figsize=(12, 6))
        df_time['year'].value_counts().sort_index().plot(kind='line', marker='o')
        plt.title("Crash Frequency Over Time")
        plt.xlabel("Year")
        plt.ylabel("Number of Crashes")
        plt.grid()
        plt.tight_layout()
        plt.show()
