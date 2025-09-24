import pandas as pd
import numpy as np

# Function that applies sin and cos in day/month
def cyclical_transform(X: pd.DataFrame) -> pd.DataFrame:
    X_new = X.copy()

    month_map = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4,
        'may': 5, 'jun': 6, 'jul': 7, 'aug': 8,
        'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }

    X_new["month_num"] = X_new["month"].map(month_map)

    # day (1–31)
    X_new["day_sin"] = np.sin(2 * np.pi * X_new["day_of_month"] / 31)
    X_new["day_cos"] = np.cos(2 * np.pi * X_new["day_of_month"] / 31)

    # month (1–12)
    X_new["month_sin"] = np.sin(2 * np.pi * X_new["month_num"] / 12)
    X_new["month_cos"] = np.cos(2 * np.pi * X_new["month_num"] / 12)

    # drop original columns
    X_new = X_new.drop(columns=["day_of_month", "month", "month_num"])
    return X_new