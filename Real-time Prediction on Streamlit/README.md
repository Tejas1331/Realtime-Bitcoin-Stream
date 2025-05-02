# 🪙 Real-Time Bitcoin Price Prediction and Streaming Dashboard

This project builds a real-time Bitcoin price tracking and prediction system using Binance WebSocket API, Kafka, an LSTM model for forecasting, Google Sheets for logging, and a Streamlit dashboard for visualization.

---

## 📁 Project Structure

```
bitcoin-realtime-pipeline/
│
├── Bitcoin Realtime Stream Producer.py           # Streams real-time BTC/USDT trade data from Binance to Kafka
├── LSTM realtime prediction to Google sheets.ipynb # Consumes Kafka messages, performs aggregation + prediction, logs to Google Sheets
├── Streamlit-dashboard.py# Streamlit dashboard to visualize actual vs predicted Bitcoin prices
├── bitcoin_lstm_model_with_buffer_Mark-2.keras # Pre-trained LSTM model (required)
├── your-creds.json             # Google Service Account credentials (required for Google Sheets access)
└── README.md                   # You are here
```

---

## 🚀 Features

- 🔁 Real-time Bitcoin trade data ingestion via Binance WebSocket API
- 📤 Kafka-based message pipeline with Avro serialization
- 🤖 LSTM-based prediction of future Bitcoin prices (2 minutes ahead)
- 🧾 Live data logging (actual + predicted prices) into a Google Sheet
- 📊 Interactive Streamlit dashboard to visualize price trends and model predictions

---

## 🛠️ Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

**`requirements.txt`** should include:
```
websocket-client
confluent_kafka
gspread
oauth2client
numpy
pandas
tensorflow
matplotlib
streamlit
```

---

## 🔑 Setup

### 1. Kafka & Schema Registry
- Set up a Kafka cluster and Schema Registry.
- Replace the placeholder values in each file:
  - `bootstrap.servers`, `sasl.username`, `sasl.password`
  - `schema_registry.url`, `schema_registry.basic.auth.user.info`

### 2. Google Sheets
- Create a Google Sheet titled **"BitcoinRealtimeData"**
- Share the sheet with your Google Service Account email.
- Place your credentials in a file named `your-creds.json` (for local use) and in Streamlit secrets (for deployment).

### 3. Streamlit Secrets Setup

Create a `.streamlit/secrets.toml`:

```toml
[gcp]
type = "service_account"
project_id = "..."
private_key_id = "..."
private_key = "..."
client_email = "..."
client_id = "..."
auth_uri = "..."
token_uri = "..."
auth_provider_x509_cert_url = "..."
client_x509_cert_url = "..."
```

---

## ▶️ How It Works

### 🧩 1. **`Bitcoin Realtime Stream Producer.py`**  
Connects to Binance WebSocket, consumes live `btcusdt@trade` prices, and pushes them to the Kafka topic `bitcoin_stream` using Avro serialization.

### 📉 2. **`LSTM realtime prediction to Google sheets.ipynb`**  
Consumes from the `bitcoin_stream` topic. It:
- Aggregates prices per minute.
- Maintains a buffer of 60 minutes.
- Uses an LSTM model to predict the price 2 minutes ahead.
- Logs `timestamp`, `1-min average price`, and `prediction` to Google Sheets.

### 📊 3. **`Streamlit-dashboard.py`**  
Fetches data from Google Sheets and renders an interactive, auto-updating dashboard using Streamlit:
- Line chart comparing actual vs predicted Bitcoin prices
- Live refresh every few seconds

---

## 🧠 Model Details

- The LSTM model (`bitcoin_lstm_model_with_buffer_Mark-2.keras`) expects a 60-minute window of average prices.
- Prediction is made for the price 2 minutes into the future.
- Input data is min-max scaled dynamically within the 60-min window + buffer to handle volatility.

---

## 🧪 Running the Pipeline

Run each of these scripts in separate terminals:

```bash
# Terminal 1: WebSocket Producer
python Bitcoin Realtime Stream Producer.py 

# Terminal 2: Kafka Consumer & Predictor
python LSTM realtime prediction to Google sheets.ipynb

# Terminal 3: Streamlit Dashboard
streamlit run Streamlit-dashboard.py
```

---

## 📦 Notes

- Ensure your Kafka and Schema Registry services are publicly accessible or run in the same network environment.
- Adjust any model prediction smoothing, scaling logic, or window size based on real-world accuracy.

---

## 📧 Contact

Feel free to reach out for collaborations or queries!
Email at - tejas.joshi959999@gmail.com

---
