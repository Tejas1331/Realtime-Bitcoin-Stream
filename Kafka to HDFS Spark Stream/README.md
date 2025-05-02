## 📦 Kafka to HDFS Spark Stream (Bitcoin Price Aggregator)

This module consumes real-time Bitcoin price data from a Kafka topic, aggregates it minute-wise, and writes the results to HDFS in partitioned Parquet format. The setup ensures efficient future access for analytical or machine learning workloads.

### 🔧 Components Used:
- **Confluent Kafka** (Confluent setup with Avro serialization)
- **GCP Spark (PySpark)**
- **HDFS**
- **Avro Schema Registry**

### 🔄 Process Flow:
1. **Consumer Setup:**
   - Connects to a Kafka topic (`bitcoin_stream`)
   - Uses Avro deserialization with schema fetched dynamically from Confluent Schema Registry

2. **Minute-level Aggregation:**
   - Buffers incoming prices by timestamp minute
   - Calculates average price for each completed minute

3. **Spark Write to HDFS:**
   - Writes aggregated data as a Spark DataFrame
   - Partitioned by `year`, `month`, `day`, and `hour` for query efficiency
   - Format: **Parquet**

4. **Graceful Shutdown Support:**
   - On keyboard interrupt or shutdown, writes any remaining buffered data to HDFS

### 📁 Output Structure:
Parquet files are written under:

```bash
hdfs:///bitcoin_stream_new/year=YYYY/month=MM/day=DD/hour=HH/
```

Each row in the Parquet file contains:
- `year`
- `month`
- `day`
- `hour`
- `minute`
- `price` (minute-wise average)

### 🛡️ Reliability Features:
- `auto.offset.reset = latest` for real-time only
- `auto.commit.interval.ms = 5000` to avoid offset loss
- Buffer is flushed on minute change or shutdown

---
