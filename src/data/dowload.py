import os
from ucimlrepo import fetch_ucirepo

DATA_DIR = "data/raw"
os.makedirs(DATA_DIR, exist_ok=True)

FEATURES_FILE = os.path.join(DATA_DIR, "features.parquet")
TARGET_FILE = os.path.join(DATA_DIR, "target.parquet")

def download_dataset():
    """
    Downloads the Bank Marketing dataset from UCIMLRepo,
    splits into features and target, and saves them as Parquet files.
    """
    dataset = fetch_ucirepo(id=222)
    X = dataset.data.features
    y = dataset.data.targets

    X.to_parquet(FEATURES_FILE, index=False)
    y.to_parquet(TARGET_FILE, index=False)

    return {
        "features_shape": X.shape,
        "targets_shape": y.shape,
        "features_path": FEATURES_FILE,
        "targets_path": TARGET_FILE
    }
