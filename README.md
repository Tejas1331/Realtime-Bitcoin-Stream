# 📊 Real-Time Crypto Price Forecasting and Aggregation using Kafka, Spark, LSTM, and Streamlit

This project demonstrates an end-to-end real-time data pipeline and forecasting system for cryptocurrency prices (e.g., Bitcoin) using a combination of **Confluent Kafka**, **GCP Spark**, **Google Cloud Platform**, **Hadoop HDFS**, **Hive**, **LSTM neural networks**, and **Streamlit**.

The system is capable of:
- Streaming real-time price data from Binance to Kafka.
- Processing and aggregating data using Spark on GCP.
- Forecasting prices using an LSTM model.
- Storing data in HDFS and Google Sheets.
- Visualizing live data and predictions in Streamlit.

---

## 🖥️ Project Dashboard

![Streamlit Dashboard](Images/Screenshot%202025-04-29%20215116.png)


---

## 📁 Project Structure

```
project-root/
│
├── 1_Hadoop_Commands/
│   └── Hadoop Necessary Commands.txt               # Basic Hadoop commands used during the project
│
├── 2_Hive_Commands/
│   └── Hive Table Creation.txt          # HiveQL commands to create and manage tables
│
├── 3_Kafka/
│   └── Kafka Schema for Key and Value.txt                      # Avro schema for Kafka key and value messages
│
├── 4_LSTM_Model/
│   ├── Bitcoin data collector for LSTM model.py       # Collecting data for training of LSTM model
│   └── lstm_model_training.ipynb                 # LSTM model training using the collected data
│
├── 5_ Kafka to HDFS Spark Stream/
│   └── Bitcoin_Consumer-Spark-HDFS.ipynb      # Processes results from kafka and dumps aggregated results into HDFS
│   
│
├── 6_Real-time Prediction on Streamlit/
│   ├── Bitcoin Realtime Stream Producer.py             # Streams real-time price data from Binance to Kafka
│   ├── LSTM realtime prediction to Google sheets.ipynb         # Spark consumer that aggregates and stores data and prediction in Google Sheets for streamlit to read from.
│   └── Streamlit-dashboard.py          # Visual dashboard showing live price and predictions
│
└── README.md                            # This master README
```

---

## 🚀 Tech Stack

| Component               | Technology Used                   |
|------------------------|-----------------------------------|
| Data Source            | Binance API                       |
| Messaging Queue        | Confluent Kafka                   |
| Stream Processing      | Spark (running on GCP)            |
| Storage                | HDFS, Google Sheets               |
| Model                  | LSTM Neural Network (TensorFlow/Keras) |
| Visualization          | Streamlit                         |
| Query Layer            | Hive (running on GCP)                              |
| Orchestration          | Manual + Custom Scripts           |

---

## 📌 Key Features

- **Modular architecture** with separate components for ingestion, processing, modeling, and visualization.
- **Real-time aggregation and prediction**.
- **Multiple sinks**: Data is stored in both HDFS (for querying via Hive) and Google Sheets (for easy sharing).
- **Visualization** built with Streamlit for end-users to see predictions and live data.

---

## ⚙️ Setup & Requirements

Due to dependencies on Kafka, Spark, GCP, and HDFS, this project requires the following setup (not plug-and-play):

- Kafka broker running (on Confluent)
- Spark environment configured (GCP)
- HDFS cluster running (GCP)
- Hive installed and connected to HDFS
- Binance API key (if using authenticated endpoints)
- Google Sheets API credentials (for write access)
- Python (with libraries: `pyspark`, `confluent-kafka`, `streamlit`, `tensorflow`, etc.)

---

## 🔐 Legal & Compliance

- Binance’s API can be used for free, and as per Binance’s terms, you're allowed to access public market data for research and non-commercial purposes.
- Do **not** use this for live trading or financial advice. This is a demo project for educational purposes only.

---

## 📎 License

This project is licensed under the ![MIT LICENSE](LICENSE). This project is for educational and research purposes. You are free to fork, learn from, and build upon this for your own research.

---
