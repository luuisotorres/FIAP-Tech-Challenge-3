from ucimlrepo import fetch_ucirepo
import pandas as pd


def download_dataset(dataset_path: str):
    """
    Downloads the Bank Marketing dataset from UCIMLRepo,
    splits into features and target, and saves them as Parquet files.
    """
    dataset = fetch_ucirepo(id=222)
    X = dataset.data.features
    y = dataset.data.targets

    df = pd.concat([X, y], axis=1)
    df.to_parquet(dataset_path, index=False)

    return {
        "features_shape": X.shape,
        "targets_shape": y.shape,
        "dataset_path": dataset_path
    }
