# 📊 Real-Time Crypto Price Forecasting and Aggregation using Kafka, Spark, LSTM, and Streamlit

This project demonstrates an end-to-end real-time data pipeline and forecasting system for cryptocurrency prices (e.g., Bitcoin) using a combination of **Apache Kafka**, **Apache Spark**, **Google Cloud Platform**, **Hadoop HDFS**, **Hive**, **LSTM neural networks**, and **Streamlit**.

The system is capable of:
- Streaming real-time price data from Binance.
- Processing and aggregating data using Spark on GCP.
- Forecasting prices using an LSTM model.
- Storing data in HDFS and Google Sheets.
- Visualizing live data and predictions in Streamlit.

---

## 📁 Project Structure

```
project-root/
│
├── 1_Hadoop_Commands/
│   └── hadoop_commands.txt               # Basic Hadoop commands used during the project
│
├── 2_Hive_Commands/
│   └── hive_table_creation.hql          # HiveQL commands to create and manage tables
│
├── 3_Kafka_Schema/
│   └── schema.avsc                      # Avro schema for Kafka key and value messages
│
├── 4_LSTM_Model/
│   ├── preprocess.py                    # Data preprocessing scripts
│   ├── train_lstm.py                    # Code to train LSTM model
│   └── model_utils.py                   # Helper functions for the LSTM model
│
├── 5_Kafka_Spark_HDFS_Integration/
│   ├── kafka_consumer.py                # Consumes Kafka stream and processes it with Spark
│   └── spark_hdfs_sink.py               # Dumps aggregated results into HDFS
│
├── 6_RealTime_Streaming/
│   ├── binance_producer.py              # Streams real-time price data from Binance to Kafka
│   ├── spark_aggregator_gcp.py          # Spark consumer that aggregates and stores in Google Sheets
│   └── streamlit_dashboard.py           # Visual dashboard showing live price and predictions
│
└── README.md                            # This master README
```

---

## 🚀 Tech Stack

| Component               | Technology Used                   |
|------------------------|-----------------------------------|
| Data Source            | Binance API                       |
| Messaging Queue        | Apache Kafka                      |
| Stream Processing      | Apache Spark (running on GCP)     |
| Storage                | HDFS, Google Sheets               |
| Model                  | LSTM Neural Network (TensorFlow/Keras) |
| Visualization          | Streamlit                         |
| Query Layer            | Apache Hive                       |
| Orchestration          | Manual + Custom Scripts           |

---

## 📌 Key Features

- **Modular architecture** with separate components for ingestion, processing, modeling, and visualization.
- **Real-time aggregation** and prediction.
- **Multiple sinks**: Data is stored in both HDFS (for querying via Hive) and Google Sheets (for easy sharing).
- **Visualization** built with Streamlit for end-users to see predictions and live data.

---

## ⚙️ Setup & Requirements

Due to dependencies on Kafka, Spark, GCP, and HDFS, this project requires the following setup (not plug-and-play):

- Kafka broker running (local or on GCP)
- Spark environment configured (GCP or local)
- HDFS cluster running
- Hive installed and connected to HDFS
- Binance API key (if using authenticated endpoints)
- Google Sheets API credentials (for write access)
- Python (with libraries: `pyspark`, `kafka-python`, `streamlit`, `tensorflow`, etc.)

---

## 🔐 Legal & Compliance

- Binance’s API can be used for free, and [as per Binance’s terms](https://binance-docs.github.io/apidocs/spot/en/#general-info), you're allowed to access public market data for research and non-commercial purposes.
- Do **not** use this for live trading or financial advice. This is a demo project for educational purposes only.

---

## 📎 License

This project is for educational and non-commercial use. You are free to fork, learn from, and build upon this for your own research.

---
