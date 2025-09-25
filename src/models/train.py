import pandas as pd
import joblib
from lightgbm import LGBMClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, PowerTransformer, FunctionTransformer
from src.config import RANDOM_SEED
from src.models.transforms import cyclical_transform

PARAMS = {
    'learning_rate': 0.050623168535997125,
    'max_iter': 1390,
    'max_leaf_nodes': 2260,
    'max_depth': 9,
    'min_samples_leaf': 41,
    'l2_regularization': 1.1298645707113427e-07,
    'max_bins': 213,
}

CATEGORICAL_FEATURES = [
    'job', 'marital', 'education',
    'default', 'housing', 'loan',
    'contact', 'poutcome',
]

NUMERICAL_FEATURES = [
    'age', 'balance', 'campaign',
    'pdays', 'previous',
]

CYCLICAL_FEATURES = [
    'month_sin', 'month_cos',
    'day_sin', 'day_cos',
]


def train_and_save_model(train_file: str, model_out: str):
    """    
    Train a machine learning classification model using the processed training dataset 
    and save the fitted model to disk.

    Steps:
        1. Load the processed training data from parquet file.
        2. Split the dataset into features (X) and target (y).
        3. Train the model with LGBMClassifier.
        4. Persist the trained model to the specified output path.

    Args:
        train_path (str): Path to the processed training dataset.
        model_out (str): Path where the trained model will be saved.

    Returns:
        str: The path to the saved model file.
    """

    train = pd.read_parquet(train_file)
    X_train = train.drop(columns=['y'])
    y_train = train['y']

    # Pipeline
    cyclical_transformer = FunctionTransformer(cyclical_transform)

    preprocessor_transformer = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), CATEGORICAL_FEATURES),
            ('num', PowerTransformer(method='yeo-johnson'), NUMERICAL_FEATURES),
            ('cyclical', 'passthrough', CYCLICAL_FEATURES),
        ],
        remainder='passthrough'
    )

    lgbm_model = LGBMClassifier(
        **PARAMS,
        random_state=RANDOM_SEED,
        n_jobs=-1,
        verbose=-1,
    )

    pipeline = Pipeline([
        ("cyclical", cyclical_transformer),
        ("preprocessor", preprocessor_transformer),
        ("classifier", lgbm_model),
    ])

    pipeline.fit(X_train, y_train)
    joblib.dump(pipeline, model_out)

    return model_out