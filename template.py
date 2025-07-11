import os
from pathlib import Path
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "aviation_crash"

# List of files and directories to be created
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/data_ingestion.py",
    f"src/{project_name}/data_cleaning.py",
    f"src/{project_name}/eda.py",
    f"src/{project_name}/clustering.py",
    f"src/{project_name}/classification.py",
    f"src/{project_name}/forecasting.py",
    f"src/{project_name}/anomaly_detection.py",
    f"src/{project_name}/utils.py",
    "data/.gitkeep",
    "models/.gitkeep",
    "notebooks/01_data_cleaning.ipynb",
    "notebooks/02_eda.ipynb",
    "notebooks/03_clustering.ipynb",
    "notebooks/04_classification.ipynb",
    "notebooks/05_forecasting.ipynb",
    "notebooks/06_anomaly.ipynb",
    "website/index.html",
    "config/config.yaml",
    "requirements.txt",
    "README.md",
    "setup.py",
]

# Creating directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filename}")
