# 📈 Real-Time Bitcoin Price Prediction

This project contains three Python scripts that together build, predict, and visualize real-time Bitcoin prices with a 2-minute offset using a machine learning model and a Google Sheet as the data store.

## 📁 Contents

- **model_training_and_pipeline.py**  
  Trains an XGBoost regression model on historical Bitcoin data and saves the preprocessing pipeline.

- **preprocessing_and_prediction.py**  
  Loads the latest data, applies the saved pipeline, makes a t+2 price prediction, and logs the result to Google Sheets.

- **real_time_streamlit_dashboard.py**  
  A Streamlit dashboard that reads real-time data from Google Sheets and displays:
  - Actual vs. Predicted prices (live plot)
  - Buy/Sell signals
  - Simulated profit/loss

## ⚙️ How to Use

1. **Train the Model:**
   ```bash
   python model_training_and_pipeline.py
   ```

2. **Run Real-Time Prediction:**
   ```bash
   python preprocessing_and_prediction.py
   ```

3. **Launch Streamlit Dashboard:**
   ```bash
   streamlit run real_time_streamlit_dashboard.py
   ```

Make sure you have:
- A trained model and preprocessing pipeline saved (done in step 1).
- A Google Sheet shared with your Google Service Account.
- Google Sheets API credentials available via `.streamlit/secrets.toml`.

## 🔐 Google Sheets API Setup

1. Enable the Google Sheets API and create a service account key.
2. Store your credentials in `.streamlit/secrets.toml`:

```toml
[gcp]
type = "service_account"
project_id = "..."
private_key_id = "..."
private_key = "..."
client_email = "..."
client_id = "..."
token_uri = "https://oauth2.googleapis.com/token"
```

3. Share your target Google Sheet with `client_email`.

---

This folder forms a minimal real-time ML pipeline connected to a live dashboard. Ideal for Bitcoin price experiments.
```
