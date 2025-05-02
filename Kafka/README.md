### 📂 Kafka

This folder contains Avro schema definitions used for the **Key** and **Value** of messages sent to the Kafka topic related to real-time Bitcoin price streaming.

These schemas are used in conjunction with Confluent Kafka's **Schema Registry** to enable strongly typed data exchange between Kafka producers and consumers.

---

### 📝 Avro Schemas

#### 1. **Value Schema**
The value schema represents the structure of the Bitcoin price data being streamed.
```json
{
  "fields": [
    {
      "logicalType": "timestamp-millis",
      "name": "timestamp",
      "type": "string"
    },
    {
      "name": "price",
      "type": "string"
    }
  ],
  "name": "BitcoinPrice",
  "namespace": "Bitcoin_Topic",
  "type": "record"
}
```

#### 2. **Key Schema**
The key schema identifies each record uniquely based on its timestamp.
```json
{
  "fields": [
    {
      "logicalType": "timestamp-millis",
      "name": "timestamp",
      "type": "string"
    }
  ],
  "name": "BitcoinKey",
  "namespace": "Bitcoin_topic_key",
  "type": "record"
}
```

---

### ⚙️ Assumptions & Requirements

- ✅ The user is expected to have a working **Confluent Kafka** setup.
- ✅ A Kafka **Cluster API Key** and **Schema Registry Key** should be configured.
- ✅ Kafka **topics** should be created beforehand.
- ✅ The Avro schemas must be **registered with the Confluent Schema Registry** before they are used by producers/consumers.

---

### 🔗 Use Case

These schemas are crucial for:
- Ensuring **data integrity** and **schema validation** during Kafka streaming.
- Supporting downstream processing with tools like **Kafka Streams**, **Spark**, or **Flink**.

---
