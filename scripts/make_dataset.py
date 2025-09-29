from src.data.download import download_dataset
from src.data.preprocess import clean_data
from src.data.split import split_train_test
from src.config import RAW_DATASET_FILE, CLEAN_DATASET_FILE, TRAIN_FILE, TEST_FILE

def main():
    print("Downloading dataset...")
    download_dataset(RAW_DATASET_FILE)
    print("Cleaning the data...")
    clean_data(RAW_DATASET_FILE, CLEAN_DATASET_FILE)
    print("Splitting the data into training and testing sets...")
    split_train_test(CLEAN_DATASET_FILE, TRAIN_FILE, TEST_FILE)
    print("Dataset processing completed!")

if __name__ == '__main__':
    main()