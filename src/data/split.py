import pandas as pd
from sklearn.model_selection import train_test_split
from src.config import RANDOM_SEED


def split_train_test(clean_dataset: str, train_file: str, test_file: str):
    df = pd.read_parquet(clean_dataset)

    train, test = train_test_split(
        df, test_size=0.2, random_state=RANDOM_SEED, stratify=df['y'],
    )

    train.to_parquet(train_file)
    test.to_parquet(test_file)

    return train, test