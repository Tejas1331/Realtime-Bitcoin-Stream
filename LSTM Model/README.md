### 📂 LSTM Model

This folder contains two files:
1. A **WebSocket-based streaming script** to collect live Bitcoin prices.
2. A **model training script** that builds and trains an LSTM model to predict Bitcoin prices based on historical trends.

---

### 🧩 File 1: `bitcoin_price_stream.py` (WebSocket Stream to CSV)

- **Purpose:**  
  Collects live trade data for Bitcoin from Binance via WebSocket and aggregates prices **per minute**.

- **Key Features:**
  - Connects to Binance's trade stream (`btcusdt@trade`).
  - Every time the minute changes, it computes the **average price** of that minute.
  - Writes the timestamped average price to a CSV file (`bitcoin_price_stream.csv`).
  - Handles disconnections and reconnects gracefully.
  - Captures Ctrl+C (SIGINT) to save any remaining buffered data before shutdown.

---

### 📈 File 2: `lstm_model_train.py` (Model Training and Evaluation)

- **Purpose:**  
  Reads the `bitcoin_price_stream.csv` file and trains an LSTM (Long Short-Term Memory) neural network model to predict the next Bitcoin price.

- **Key Steps:**
  - Loads average minute-wise prices from the CSV file.
  - Prepares **input-output sequences** using a sliding window approach.
  - Scales each training window with **min-max normalization**, applying a small buffer to avoid edge effects.
  - Splits data into **training and testing** sets.
  - Builds and trains a **2-layer LSTM model** using Keras.
  - Converts predictions back to original price scale using stored min-max values.
  - Visualizes predicted vs. actual prices.
  - Computes error metrics: **MAE** (Mean Absolute Error) and **MAPE** (Mean Absolute Percentage Error).
  - Saves the trained model and min-max scaling values for future use.

---

### ⚙️ Assumptions

- The live stream and model training are expected to be run **independently** — i.e., the stream must collect enough historical data before training.
- The user should run the WebSocket collector long enough to gather sufficient data (e.g., a few hours) before model training.

---
