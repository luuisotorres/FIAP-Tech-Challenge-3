import os

RANDOM_SEED = 42

# Root data folder
DATA_DIR = "data"

# Subfolders
RAW_DIR = os.path.join(DATA_DIR, "raw")
INTERIM_DIR = os.path.join(DATA_DIR, "interim")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")

# Specific files (raw)
RAW_DATASET_FILE = os.path.join(RAW_DIR, "dataset.parquet")

# Specific files (interim)
CLEAN_DATASET_FILE = os.path.join(INTERIM_DIR, "clean_dataset.parquet")

# Specific files (processed)
TRAIN_FILE = os.path.join(PROCESSED_DIR, "train.parquet")
TEST_FILE = os.path.join(PROCESSED_DIR, "test.parquet")

# Models
MODELS_DIR = "models"
BEST_MODEL_FILE = os.path.join(MODELS_DIR, "best_model.joblib")

# Reports
REPORTS_DIR = "reports"
METRICS_FILE = os.path.join(REPORTS_DIR, "metrics.json")