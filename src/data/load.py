import pandas as pd
from ucimlrepo import fetch_ucirepo

def load_raw_data(path: str = "data/raw/bank_marketing.csv") -> pd.DataFrame:
    """
    Fetch Bank Marketing dataset from UCI (id=222) and save a raw CSV copy.
    If file already exists locally, just load it.
    """
    try:
        # try load from local cache
        df = pd.read_csv(path)
        print(f"Loaded raw dataset from {path}")
    except FileNotFoundError:
        # fetch from UCI repo
        bank_marketing = fetch_ucirepo(id=222)
        X = bank_marketing.data.features
        y = bank_marketing.data.targets
        df = pd.concat([X, y], axis=1)
        df.to_csv(path, index=False)
        print(f"Fetched from UCI and saved to {path}")
    return df
