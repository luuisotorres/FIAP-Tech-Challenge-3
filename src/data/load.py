import os
import pandas as pd

DATA_DIR = "data/raw"
os.makedirs(DATA_DIR, exist_ok=True)

FEATURES_FILE = os.path.join(DATA_DIR, "features.parquet")
TARGET_FILE = os.path.join(DATA_DIR, "target.parquet")

def load_dataset():
    X = pd.read_parquet(FEATURES_FILE)
    y = pd.read_parquet(TARGET_FILE)
    
    df = pd.concat([X, y], axis=1)
    
    return df