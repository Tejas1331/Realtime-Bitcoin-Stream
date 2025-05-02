import websocket
import json
import time
import datetime
import csv
import threading
import signal
import os

stop_event = threading.Event()
reconnect_event = threading.Event()

buffer = []
current_minute = None
csv_file = "bitcoin_price_stream.csv"

# Create CSV file with headers if not exists
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["year", "month", "day", "hour", "minute", "avg_price"])

def aggregate_and_save(prices, minute_key):
    if prices:
        avg_price = sum(prices) / len(prices)
        year, month, day, hour, minute = minute_key

        with open(csv_file, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([year, month, day, hour, minute, avg_price])

        print(f"[{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}] Avg price: {avg_price:.2f} written to CSV.")

def on_message(ws, message):
    global buffer, current_minute

    try:
        data = json.loads(message)
        price = float(data['p'])
        timestamp = datetime.datetime.now()
        minute_key = (timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute)

        if current_minute is None:
            current_minute = minute_key

        if minute_key == current_minute:
            buffer.append(price)
        else:
            # Minute changed, aggregate and reset
            aggregate_and_save(buffer, current_minute)
            buffer = [price]
            current_minute = minute_key

    except Exception as e:
        print(f"❌ Error processing message: {e}")

def on_error(ws, error):
    print(f"⚠️ WebSocket Error: {error}")
    reconnect_event.set()
    ws.close()

def on_close(ws, close_status_code, close_msg):
    print(f"❌ WebSocket closed: {close_status_code} {close_msg}")
    reconnect_event.set()

def on_open(ws):
    payload = {
        "method": "SUBSCRIBE",
        "params": ["btcusdt@trade"],
        "id": 1
    }
    ws.send(json.dumps(payload))

def start_websocket():
    while not stop_event.is_set():
        reconnect_event.clear()
        ws = websocket.WebSocketApp(
            "wss://stream.binance.com:9443/ws/btcusdt@trade",
            on_message=on_message,
            on_error=on_error,
            on_close=on_close
        )
        ws.on_open = on_open

        print("🔁 Starting WebSocket connection...")
        wst = threading.Thread(target=ws.run_forever)
        wst.daemon = True
        wst.start()

        while not stop_event.is_set() and not reconnect_event.is_set():
            time.sleep(1)

        print("🔌 Reconnecting in 5 seconds...")
        time.sleep(5)

def signal_handler(sig, frame):
    global buffer, current_minute
    print("\n🛑 Ctrl+C detected. Saving remaining data and exiting...")
    stop_event.set()

    if buffer and current_minute:
        aggregate_and_save(buffer, current_minute)

    exit(0)

# Register Ctrl+C signal
signal.signal(signal.SIGINT, signal_handler)

# Start WebSocket stream
start_websocket()
