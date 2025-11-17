import os
import zipfile
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
ZIP_PATH = os.path.join(DATA_DIR, "data_files.zip")

def ensure_data_extracted():
    """Extracts the ZIP file if the CSV files are not already available."""
    
    expected_file = os.path.join(DATA_DIR, "player_profiles.csv")
    
    if not os.path.exists(expected_file):
        print("🔓 Extracting files from data_files.zip...")
        
        with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall(DATA_DIR)
        
        print("✔️ Files extracted successfully!")
    
    else:
        print("✔️ Data files already available.")

def load_csv(filename):
    """Loads a CSV file, ensuring data extraction first."""
    
    ensure_data_extracted()
    return pd.read_csv(os.path.join(DATA_DIR, filename))

