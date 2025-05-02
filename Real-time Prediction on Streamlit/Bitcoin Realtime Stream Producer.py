import websocket
import json
import time
import datetime
import traceback
import signal
import threading
from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import StringSerializer

# --- Kafka setup ---
kafka_config = {
    'bootstrap.servers': 'Cluster-server',
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': 'Cluster-username',
    'sasl.password': 'Cluster-password'
}

schema_registry_client = SchemaRegistryClient({
    'url': 'Schema-registry-endpoint',
    'basic.auth.user.info': 'Schema-registry-name/Schema-registry-password'
})

subject_name = 'bitcoin_stream-value'
schema_str = schema_registry_client.get_latest_version(subject_name).schema.schema_str

key_serializer = StringSerializer('utf_8')
avro_serializer = AvroSerializer(schema_registry_client, schema_str)

producer = SerializingProducer({
    **kafka_config,
    'key.serializer': key_serializer,
    'value.serializer': avro_serializer
})

stop_event = threading.Event()
reconnect_event = threading.Event()

def delivery_report(err, msg):
    if err is not None:
        print("❌ Delivery failed: {}".format(err))
    else:
        print(f"✅ Delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

def on_message(ws, message):
    try:
        time.sleep(1)
        data = json.loads(message)
        price = data['p']
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        value = {"timestamp": timestamp, "price": price}
        producer.produce(topic='bitcoin_stream', key=timestamp, value=value, on_delivery=delivery_report)
        producer.flush()
        print(f" [{timestamp}] Bitcoin Price (USD): {price} ")
    except Exception as e:
        print(f"❌ Error in message: {e}")
        traceback.print_exc()

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
    print("\n🛑 Ctrl+C detected. Stopping gracefully...")
    stop_event.set()

signal.signal(signal.SIGINT, signal_handler)

# Start WebSocket loop
start_websocket()