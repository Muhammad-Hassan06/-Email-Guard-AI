# 🛡️ Email Guard AI | Spam & Phishing Detector

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/Frontend-React%2018-61DAFB?style=for-the-badge&logo=react)](https://reactjs.org/)
[![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

An intelligent Machine Learning NLP platform designed to identify and classify emails and text messages as **Spam / Phishing** or **Legitimate (Ham)** with high precision. Powered by **TF-IDF Vectorization** and **Logistic Regression**, the system achieves **96.7% test accuracy** and features an interactive React dashboard backed by FastAPI and a dual-execution fallback architecture.

---

## ✨ Key Features

- **🔮 Interactive Spam Classifier:** Input custom text or test pre-loaded presets (Prize Scam, Work Email, Security Alert) with instant probability breakdown.
- **📊 Interactive Dataset Analytics:** Visual breakdown of dataset distribution (5,572 messages) powered by Chart.js.
- **⚠️ Trigger Pattern Extraction:** Automatically highlights suspicious keywords (e.g., *winner*, *claim*, *urgent*, *verify*, *suspended*).
- **🔬 Model Specs & Pipeline View:** Detailed look at the TF-IDF feature extraction pipeline and binary classifier metrics.
- **⚡ Dual-Execution Engine:** 
  - 🟢 **Live FastAPI Backend:** Connects to `http://localhost:8000/predict` to inference `spam_ham_model.pkl` & `tfidf_vectorizer.pkl`.
  - ⚡ **Client-Side Fallback Engine:** Gracefully handles offline states using heuristic pattern matching so the UI remains fully operational.
- **🔌 OpenAPI / Swagger Documentation:** Integrated Swagger UI for testing API endpoints directly.

---

## 🛠️ Tech Stack & Architecture

- **Frontend:** React 18 (Standalone UI), CSS3 Glassmorphism UI, Chart.js Analytics
- **Backend API:** FastAPI, Uvicorn ASGI Server, Pydantic Schema Validation
- **Machine Learning:** Scikit-Learn (TF-IDF Vectorizer, Logistic Regression), Pandas, NumPy
- **Storage / Artifacts:** Pickle serialized model files (`spam_ham_model.pkl`, `tfidf_vectorizer.pkl`)

---

## 🔬 Machine Learning Model Details

| Metric / Parameter | Specification |
| :--- | :--- |
| **Dataset Size** | 5,572 messages (4,825 Ham / 747 Spam) |
| **Feature Extraction** | `TfidfVectorizer` (English stop words removal, lowercase normalization) |
| **Classifier Model** | Logistic Regression |
| **Train / Test Split** | 80% Train / 20% Test |
| **Training Accuracy** | **96.77%** |
| **Testing Accuracy** | **96.68%** |

---

## 🔌 API Reference

### 1. Predict Spam / Ham
- **Endpoint:** `POST /predict`
- **Headers:** `Content-Type: application/json`

**Request Body:**
```json
{
  "text": "WINNER!! As a valued network customer you have been selected to receive a £900 prize reward! Call 09061701461 to claim your reward."
}
```

**Response:**
```json
{
  "label": "Spam",
  "is_spam": true,
  "confidence": 0.985,
  "spam_probability": 0.985,
  "ham_probability": 0.015
}
```

---

## 🚀 Getting Started

### 1. Prerequisites & Installation

Clone the repository and install the Python dependencies:

```bash
git clone https://github.com/Muhammad-Hassan06/AI_MODEL_BACKEND.git
cd "05-spam-email-detector"
pip install fastapi uvicorn pydantic scikit-learn pandas numpy
```

### 2. Launch the FastAPI Backend

Run the backend server using Uvicorn:

```bash
python -m uvicorn main:app --reload --port 8000
```

- API Base URL: `http://localhost:8000`
- Interactive Swagger UI: `http://localhost:8000/docs`

### 3. Open the Frontend UI

Simply open **`index.html`** in any modern web browser or use Live Server.

---

## 📂 Project Structure

```
05-spam-email-detector/
├── main.py                 # FastAPI backend server with /predict endpoint
├── index.html              # React 18 interactive frontend dashboard
├── style.css               # Modern glassmorphism dark theme styling
├── spam_ham_model.pkl      # Trained Scikit-Learn Logistic Regression model
├── tfidf_vectorizer.pkl    # Serialized TF-IDF text feature vectorizer
├── train_model.ipynb       # Jupyter notebook for model training & evaluation
├── mail_data.csv           # Email dataset (5,572 rows)
└── README.md               # Project documentation
```

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

"# -Email-Guard-AI" 
