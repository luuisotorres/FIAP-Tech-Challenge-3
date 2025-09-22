"""
Tech Challenge 3 - FIAP

API for ingestion and initial processing of the Bank Marketing dataset (UCI repository).

Functionalities:
- Uses the ucimlrepo package to import the dataset.
- Converts the dataset to Parquet format.
- Overwrites the Parquet file if it already exists.
- Provides an endpoint to view features and targets.
- Provides an endpoint to display the dataset as an HTML table.

Authors: 
    Izabelly de Oliveira Menezes, 
    Larissa Diniz da Silva, 
    Luis Fernando Torres, 
    Rafael dos Santos Callegari, 
    Renato Massamitsu Zama Inomata
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import pandas as pd
import os
from src.data.dowload import download_dataset
from src.data.load import load_dataset

# MAIN FASTAPI APPLICATION INSTANCE
app = FastAPI(
    title="Tech Challenge 3 - Bank Marketing API",
    description="API to download, process, and store the Bank Marketing dataset in Parquet format.",
    version="1.0.0"
)

# DIRECTORY WHERE DATA WILL BE STORED
DATA_DIR = "data/raw"
os.makedirs(DATA_DIR, exist_ok=True)

# PATHS FOR PARQUET FILES
FEATURES_FILE = os.path.join(DATA_DIR, "features.parquet")
TARGET_FILE = os.path.join(DATA_DIR, "target.parquet")


@app.get("/")
def root():
    """
    Root endpoint of the API.
    """
    return {"message": "Tech Challenge 3 - Bank Marketing API"}


@app.get("/download")
def download():
    """
    Downloads the dataset using ucimlrepo, separates features and targets,
    and saves them as Parquet files. Overwrites old files if they exist.
    """
    try:
        result = download_dataset()
        return {"message": "Dataset successfully downloaded.", **result}
    except Exception as e:
        return {"error": str(e)}
    


@app.get("/dataset", response_class=HTMLResponse)
def get_dataset_table():
    """
    Returns an HTML table with features and target data.
    """
    # if not os.path.exists(FEATURES_FILE) or not os.path.exists(TARGET_FILE):
    #     return HTMLResponse(content="<h3>Dataset has not been downloaded yet. Please use /download first.</h3>", status_code=404)

    # X = pd.read_parquet(FEATURES_FILE)
    # y = pd.read_parquet(TARGET_FILE)

    # # COMBINE FEATURES AND TARGETS
    # df = pd.concat([X, y], axis=1)
    try:
        df = load_dataset()
        
    except Exception as e:
        print(f"Error while loading dataset: {e}")
        return HTMLResponse(content="<h3>Dataset has not been downloaded yet. Please use /download first.</h3>", status_code=404)

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
    Endpoint for the favicon.
    """
    return FileResponse("favicon.ico")