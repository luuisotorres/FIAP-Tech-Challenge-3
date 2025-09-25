from src.data.download import download_dataset
from src.data.preprocess import clean_data
from src.data.split import split_train_test
from src.config import RAW_DATASET_FILE, CLEAN_DATASET_FILE, TRAIN_FILE, TEST_FILE

def main():
    download_dataset(RAW_DATASET_FILE)
    clean_data(RAW_DATASET_FILE, CLEAN_DATASET_FILE)
    split_train_test(CLEAN_DATASET_FILE, TRAIN_FILE, TEST_FILE)

if __name__ == '__main__':
    main()