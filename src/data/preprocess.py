import pandas as pd


def clean_data(raw_dataset_path: str, clean_dataset_path: str):
    """
    Preprocess data from original raw dataset. 
    * Drops `duration` column; 
    * Fill NAs with "unknown";
    * Change `day_of_week` to `day_of_month`; 
    * Map `y` to "yes": 1 and "no": 0.
    """
    
    df_raw = pd.read_parquet(raw_dataset_path)

    df = df_raw.drop(columns=['duration'], axis=1)

    categorical_features = [
        'job', 'marital', 'education',
        'default', 'housing', 'loan', 
        'contact', 'month', 'poutcome', 
    ]

    df[categorical_features] = df[categorical_features].fillna('unknown')
    df.rename(columns={'day_of_week': 'day_of_month'}, inplace=True)
    df['y'] = df['y'].map({'yes': 1, 'no': 0})

    df.to_parquet(clean_dataset_path)

    return df