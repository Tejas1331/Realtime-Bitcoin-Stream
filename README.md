# 🔮 Real-Time Bitcoin Price Prediction System

Welcome to the **Real-Time Bitcoin Price Prediction System** — a full-stack data streaming and analytics project that demonstrates how to integrate real-time data ingestion, machine learning, and visual dashboards for cryptocurrency monitoring.

---

## 🚀 Project Overview

This project is designed to:
- **Ingest** live Bitcoin price data using Kafka.
- **Predict** future Bitcoin prices using a machine learning model (predicting t+2 minute prices).
- **Stream** the data using Apache Spark (Batch or Structured Streaming).
- **Visualize** live data and predictions in a Streamlit dashboard.
- **Track** Buy/Sell signals and profit/loss calculations.
- **Log** results and data into Google Sheets for persistence and monitoring.

---

## 🧱 Project Structure



Each folder contains a separate `README.md` to explain its specific purpose, setup, and execution steps.

---

## ⚙️ Technologies Used

- **Python** (v3.8+)
- **Apache Kafka** – for real-time data streaming
- **Apache Spark** – for data processing and inference
- **Streamlit** – for building the live dashboard
- **Google Sheets API** – for logging real-time data and predictions
- **Pandas / NumPy / Matplotlib** – for data manipulation and visualization
- **Scikit-learn** – for model training
- **Tensorflow/Keras** - LSTM Model

---

## 🛠️ Setup Instructions

> ⚠️ Note: This project is designed to run in a development or production environment where Kafka and Spark are properly configured. You will need to set up those services manually or via Docker before running the full pipeline.
