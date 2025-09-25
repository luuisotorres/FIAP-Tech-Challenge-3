# FIAP-Tech-Challenge-3
# 📊 Bank Marketing ML Project

Machine Learning Engineering project applied to the [Bank Marketing dataset (UCI)](https://archive.ics.uci.edu/dataset/222/bank+marketing).  
The goal is to predict whether a client will subscribe to a **term deposit** after a telemarketing campaign, using **supervised classification techniques**.  

---

## 📂 Project Structure

```
bank_marketing_ml/
├── data/
│   ├── raw/        # original data (UCI)
│   ├── interim/    # partially processed data
│   └── processed/  # final datasets for training/testing
│
├── frontend/       # streamlit app to run predictions
│
├── models/         # trained models (.pkl, .joblib)
│
├── notebooks/      # exploratory data analysis (EDA, prototyping)
│
├── scripts/        # pipeline entrypoints
│   ├── make_dataset.py
│   ├── train_model.py
│   └── evaluate_model.py
│
├── src/            # project source code
│   ├── data/       # ingestion and preprocessing
│   ├── models/     # training, evaluation, prediction
│   └── app/        # application (FastAPI)
│
└── reports/        # reports and figures
```

---

## ⚙️ Environment Setup

This project uses [uv](https://github.com/astral-sh/uv) as the dependency and virtual environment manager.

### 1. Clone the repository
```bash
git clone https://github.com/your-username/bank_marketing_ml.git
cd bank_marketing_ml
```

### 2. Install dependencies
```bash
uv sync
```

This will:
- Create a `.venv/` virtual environment  
- Install all dependencies listed in `pyproject.toml`  

### 3. Activate the environment
```bash
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows (PowerShell)
```

### 4. Environment Variables

This project uses environment variables to configure the application. A template file is provided to make the setup easier.

First, copy the example configuration file to a new `.env` file. This new file will be used by the application and should not be committed to version control.

* **On macOS/Linux:**
    ```bash
    cp .env.example .env
    ```
* **On Windows:**
    ```bash
    copy .env.example .env
    ```

Now, open the `.env` file and review its contents.

* `FASTAPI_URL`: This variable defines the complete base URL where your FastAPI application is running. The Streamlit front-end uses this URL to send requests to the back-end API. The default value is typically `http://127.0.0.1:8000`.
---

## ▶️ Running the Pipeline

### 1. Generate processed datasets
```bash
uv run -m scripts.make_dataset
```

### 2. Train the model
```bash
uv run -m scripts.train_model
```

<!-- ### 3. Evaluate the model
```bash
uv run scripts/evaluate_model.py
``` -->

---

## 🖥️ Application

Run the FastAPI app with:
```bash
uv run uvicorn src.app.api:app --reload
```

You can run the steamlit app with:

```bash
uv run -m streamlit run frontend/streamlit_app.py 
```

<!-- ---

## ✅ Testing

Run unit tests:
```bash
uv run pytest
```

--- -->

## 👥 Team

This project was developed for the **Machine Learning Engineering Postgraduate Program** by:  
* Izabelly de Oliveira Menezes | [Github](https://github.com/izabellyomenezes)
* Larissa Diniz da Silva | [Github](https://github.com/Ldiniz737)
* Luis Fernando Torres | [Github](https://github.com/luuisotorres)
* Rafael dos Santos Callegari | [Github](https://github.com/rafaelcallegari)
* Renato Massamitsu Zama Inomata | [Github](https://github.com/renatoinomata)