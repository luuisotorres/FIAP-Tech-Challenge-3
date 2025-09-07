# FIAP-Tech-Challenge-3

Machine Learning Engineering project applied to the [Bank Marketing dataset (UCI)](https://archive.ics.uci.edu/dataset/222/bank+marketing).  

The goal is to predict whether a client will subscribe to a **term deposit** after a telemarketing campaign, using **supervised classification techniques**.  

## 📂 Project Structure
```
FIAP-Tech-Challenge-3/
├── data/
│   ├── raw/                # original data (UCI)
│   ├── interim/            # partially processed data
│   └── processed/          # final datasets for training/testing
│
├── notebooks/              # exploratory data analysis (EDA, prototyping)
│
├── src/                    # project source code
│   ├── data/               # ingestion and preprocessing
│   ├── features/           # feature engineering
│   ├── models/             # training, evaluation, prediction
│   └── app/                # application (API or Streamlit)
│
├── scripts/                # pipeline entrypoints
│
├── models/                 # trained models (.pkl, .joblib)
│
├── reports/                # reports and figures
│
└── tests/                  # unit tests
```

## ⚙️ Environment Setup
This project uses [uv](https://github.com/astral-sh/uv) as the dependency and virtual environment manager.


### 1. Clone the repository

```bash
git clone https://github.com/seu-usuario/bank_marketing_ml.git
cd bank_marketing_ml    
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Activate the environment

```bash
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows (PowerShell)
```

## 🖥️ Application


## 👥 Authors

[Izabelly de Oliveira Menezes](https://github.com/izabellyomenezes)

[Larissa Diniz](https://github.com/Ldiniz737)

[Luis Fernando Torres](https://github.com/luuisotorres)

[Rafael Callegari](https://github.com/rafaelcallegari)

[Renato Inomata](https://github.com/renatoinomata)