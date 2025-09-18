"""
TECH CHALLENGE 3 - FIAP

API FOR INGESTION AND INITIAL PROCESSING OF THE BANK MARKETING DATASET (UCI REPOSITORY).

FUNCTIONALITIES:
- USES THE UCIMLREPO PACKAGE TO IMPORT THE DATASET.
- CONVERTS THE DATASET TO PARQUET.
- OVERWRITES THE PARQUET FILE IF IT ALREADY EXISTS.
- PROVIDES AN ENDPOINT TO VIEW FEATURES AND TARGETS.
- PROVIDES AN ENDPOINT TO DISPLAY THE DATASET AS AN HTML TABLE.

AUTHORS: IZABELLY DE OLIVEIRA MENEZES, LARISSA DINIZ DA SILVA, LUIS FERNANDO TORRES, RAFAEL DOS SANTOS CALLEGARI, RENATO MASSAMITSU ZAMA INOMATA
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import pandas as pd
import os
from ucimlrepo import fetch_ucirepo

# MAIN FASTAPI APPLICATION INSTANCE
app = FastAPI(
    title="TECH CHALLENGE 3 - BANK MARKETING API",
    description="API TO DOWNLOAD, PROCESS, AND STORE THE BANK MARKETING DATASET IN PARQUET FORMAT.",
    version="1.0.0"
)

# DIRECTORY WHERE DATA WILL BE STORED
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

# PATHS FOR PARQUET FILES
FEATURES_FILE = os.path.join(DATA_DIR, "features.parquet")
TARGET_FILE = os.path.join(DATA_DIR, "target.parquet")


@app.get("/")
def root():
    """
    ROOT ENDPOINT OF THE API
    """
    return {"message": "TECH CHALLENGE 3 - BANK MARKETING API"}


@app.get("/download")
def download_dataset():
    """
    DOWNLOADS THE DATASET USING UCIMLREPO, SEPARATES FEATURES AND TARGETS, AND SAVES THEM AS PARQUET FILES.
    OVERWRITES OLD FILES IF THEY EXIST.
    """
    try:
        # REMOVE OLD PARQUET FILES
        if os.path.exists(FEATURES_FILE):
            os.remove(FEATURES_FILE)
        if os.path.exists(TARGET_FILE):
            os.remove(TARGET_FILE)

        # FETCH DATASET FROM UCIMLREPO
        dataset = fetch_ucirepo(id=222)
        X = dataset.data.features
        y = dataset.data.targets

        # SAVE FEATURES AND TARGETS AS PARQUET
        X.to_parquet(FEATURES_FILE, index=False)
        y.to_parquet(TARGET_FILE, index=False)

        return {
            "message": "DATASET SUCCESSFULLY DOWNLOADED AND CONVERTED TO PARQUET!",
            "features_shape": X.shape,
            "targets_shape": y.shape,
            "features_path": FEATURES_FILE,
            "targets_path": TARGET_FILE
        }

    except Exception as e:
        return {"error": f"ERROR DOWNLOADING DATASET: {e}"}


@app.get("/dataset", response_class=HTMLResponse)
def get_dataset_table():
    """
    RETURNS AN HTML TABLE WITH FEATURES AND TARGETS DATA
    """
    if not os.path.exists(FEATURES_FILE) or not os.path.exists(TARGET_FILE):
        return HTMLResponse(content="<h3>DATASET HAS NOT BEEN DOWNLOADED YET. PLEASE USE /download FIRST.</h3>", status_code=404)

    X = pd.read_parquet(FEATURES_FILE)
    y = pd.read_parquet(TARGET_FILE)

    # COMBINE FEATURES AND TARGETS
    df = pd.concat([X, y], axis=1)

    # GENERATE HTML
    html_table = df.head(10).to_html(classes="table table-striped", index=False)

    html_content = f"""
    <html>
        <head>
            <title>Bank Marketing Dataset</title>
            <link rel="icon" href="/favicon.ico" type="image/x-icon" />
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        </head>
        <body>
            <div class="container mt-4">
                <h2>Bank Marketing Dataset Preview</h2>
                {html_table}
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    """
    ENDPOINT FOR FAVICON
    """
    return FileResponse("favicon.ico")