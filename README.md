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
│   ├── processed/  # final datasets for training/testing
│   └── external/   # external sources (e.g. Portuguese holidays)
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
│   ├── features/   # feature engineering
│   ├── models/     # training, evaluation, prediction
│   └── app/        # application (API or Streamlit)
│
├── models/         # trained models (.pkl, .joblib)
├── reports/        # reports and figures
└── tests/          # unit tests
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

---

## ▶️ Running the Pipeline

### 1. Generate processed datasets
```bash
uv run scripts/make_dataset.py
```

### 2. Train the model
```bash
uv run scripts/train_model.py
```

### 3. Evaluate the model
```bash
uv run scripts/evaluate_model.py
```

---

## 🖥️ Application

After training a model, you can run the app (example with **Streamlit**):

```bash
uv run streamlit run src/app/main.py
```

---

## ✅ Testing

Run unit tests:
```bash
uv run pytest
```

---

## 👥 Team

This project was developed for the **Machine Learning Engineering Postgraduate Program** by:  
- Member A – Data preprocessing  
- Member B – Modeling  
- Member C – Evaluation & metrics  
- Member D – Deployment / Application  
- Member E – Documentation & Coordination  