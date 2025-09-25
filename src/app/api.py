"""
Tech Challenge 3 - FIAP

API for ingestion and initial processing of the Bank Marketing dataset (UCI repository).

Functionalities:
- Uses the ucimlrepo package to import the dataset.
- Converts the dataset to Parquet format.
- Overwrites the Parquet file if it already exists.
- Provides an endpoint to view the dataset.
- Provides an endpoint to display the dataset as an HTML table.

Authors: 
    Izabelly de Oliveira Menezes, 
    Larissa Diniz da Silva, 
    Luis Fernando Torres, 
    Rafael dos Santos Callegari, 
    Renato Massamitsu Zama Inomata
"""

import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from data.download import download_dataset
from src.config import RAW_DATASET_FILE
from src.app.schemas import MarketingLead
from src.app.ml_model import load_model, predict


# Main FastAPI application instance
app = FastAPI(
    title="Tech Challenge 3 - Bank Marketing API",
    description="API to download, process, and store the Bank Marketing dataset in Parquet format.",
    version="1.0.0"
)

# Load model once at startup
load_model()


@app.get("/")
def root():
    """
    Root endpoint of the API.
    """
    return {"message": "Tech Challenge 3 - Bank Marketing API"}


@app.get("/download")
def download():
    """
    Downloads the dataset using ucimlrepo, and saves them as Parquet files. 
    Overwrites old files if they exist.
    """
    try:
        result = download_dataset(RAW_DATASET_FILE)
        return {"message": "Dataset successfully downloaded.", **result}
    except Exception as e:
        return {"error": str(e)}


@app.get("/dataset", response_class=HTMLResponse)
def get_dataset_table():
    """
    Returns an HTML table with the dataset.
    """

    try:
        df = pd.read_parquet(RAW_DATASET_FILE)

    except Exception as e:
        print(f"Error while loading dataset: {e}")
        return HTMLResponse(content="<h3>Dataset has not been downloaded yet. Please use /download first.</h3>", status_code=404)

    # GENERATE HTML
    html_table = df.head(10).to_html(
        classes="table table-striped", index=False)

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


@app.post("/predict")
def predict_endpoint(lead_data: MarketingLead):
    # Convert input to DataFrame
    input_df = pd.DataFrame([lead_data.model_dump()])

    # Make prediction
    try:
        pred, prob = predict(input_df)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")

    return {"prediction": pred, "probability_yes": prob}