"""
TECH CHALLENGE 3 - FIAP

API PARA INGESTÃO E TRATAMENTO INICIAL DO DATASET BANK MARKETING (UCI REPOSITORY).

FUNCIONALIDADES:
- USA O PACOTE UCIMLREPO PARA IMPORTAR O DATASET.
- CONVERTE O DATASET PARA PARQUET.
- SOBRESCREVE O ARQUIVO PARQUET CASO JÁ EXISTA.
- DISPONIBILIZA ENDPOINT PARA VISUALIZAÇÃO DE FEATURES E TARGETS.
- DISPONIBILIZA ENDPOINT PARA VISUALIZAÇÃO EM TABELA HTML.

AUTORES: IZABELLY DE OLIVEIRA MENEZES, LARISSA DINIZ DA SILVA, LUIS FERNANDO TORRES, RAFAEL DOS SANTOS CALLEGARI, RENATO MASSAMITSU ZAMA INOMATA
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import pandas as pd
import os
from ucimlrepo import fetch_ucirepo

# INSTÂNCIA PRINCIPAL DA APLICAÇÃO FASTAPI
app = FastAPI(
    title="TECH CHALLENGE 3 - BANK MARKETING API",
    description="API PARA BAIXAR, PROCESSAR E ARMAZENAR O DATASET BANK MARKETING EM PARQUET.",
    version="1.0.0"
)

# DIRETÓRIO ONDE OS DADOS SERÃO ARMAZENADOS
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

# CAMINHO DOS ARQUIVOS PARQUET
FEATURES_FILE = os.path.join(DATA_DIR, "features.parquet")
TARGET_FILE = os.path.join(DATA_DIR, "target.parquet")


@app.get("/")
def root():
    """
    ENDPOINT RAIZ DA API
    """
    return {"message": "API DO TECH CHALLENGE 3 - BANK MARKETING"}


@app.get("/download")
def download_dataset():
    """
    FAZ O DOWNLOAD DO DATASET USANDO UCIMLREPO, SEPARA FEATURES E TARGET, SALVA EM PARQUET.
    SUBSTITUI ARQUIVOS ANTIGOS CASO EXISTAM.
    """
    try:
        # REMOVER PARQUETS ANTIGOS
        if os.path.exists(FEATURES_FILE):
            os.remove(FEATURES_FILE)
        if os.path.exists(TARGET_FILE):
            os.remove(TARGET_FILE)

        # BUSCAR DATASET PELO UCIMLREPO
        dataset = fetch_ucirepo(id=222)
        X = dataset.data.features
        y = dataset.data.targets

        # SALVAR FEATURES E TARGET EM PARQUET
        X.to_parquet(FEATURES_FILE, index=False)
        y.to_parquet(TARGET_FILE, index=False)

        return {
            "message": "DATASET BAIXADO E CONVERTIDO PARA PARQUET COM SUCESSO!",
            "features_shape": X.shape,
            "targets_shape": y.shape,
            "features_path": FEATURES_FILE,
            "targets_path": TARGET_FILE
        }

    except Exception as e:
        return {"error": f"ERRO AO BAIXAR O DATASET: {e}"}


@app.get("/dataset", response_class=HTMLResponse)
def get_dataset_table():
    """
    RETORNA UMA TABELA HTML COM OS DADOS DE FEATURES E TARGETS
    """
    if not os.path.exists(FEATURES_FILE) or not os.path.exists(TARGET_FILE):
        return HTMLResponse(content="<h3>DATASET AINDA NÃO FOI BAIXADO. USE /download PRIMEIRO.</h3>", status_code=404)

    X = pd.read_parquet(FEATURES_FILE)
    y = pd.read_parquet(TARGET_FILE)

    # JUNTAR FEATURES E TARGET
    df = pd.concat([X, y], axis=1)

    # GERAR HTML
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
    ENDPOINT PARA FAVICON
    """
    return FileResponse("favicon.ico")
