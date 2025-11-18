import os
import zipfile
import pandas as pd
import warnings

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
ZIP_PATH = os.path.join(DATA_DIR, "data_files.zip")

def ensure_data_extracted():
    """Extracts the ZIP file if the CSV files are not already available."""
    
    expected_file = os.path.join(DATA_DIR, "player_profiles.csv")
    
    if not os.path.exists(expected_file):
        with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall(DATA_DIR)

def load_csv(filename):
    """Loads a CSV file, ensuring data extraction first."""
    
    ensure_data_extracted()
    
    # Suppress all warnings and messages
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return pd.read_csv(os.path.join(DATA_DIR, filename), low_memory=False)

