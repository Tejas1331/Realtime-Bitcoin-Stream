### 📂 Hive_Commands

This folder contains essential Hive commands used to define and manage the external Hive table for querying streaming Bitcoin price data stored in HDFS. These commands support the partitioned storage structure and allow efficient querying of time-series data.

---

### 📜 Commands Reference

#### 1. **Creating an External Table**
```sql
CREATE EXTERNAL TABLE IF NOT EXISTS bitcoin_data (
    minute INT,
    price DOUBLE
)
PARTITIONED BY (
    year INT,
    month INT,
    day INT,
    hour INT
)
STORED AS PARQUET
LOCATION '/bitcoin_stream_new';
```
- Defines a **partitioned** external Hive table.
- Data is stored in **Parquet** format under the given HDFS location.
- `EXTERNAL` ensures that Hive does not delete the data upon table deletion.

#### 2. **Displaying Column Headers in Hive CLI**
```sql
set hive.cli.print.header=true;
```
- Enables display of column headers when querying from the Hive CLI.

#### 3. **Repairing Table Partitions (Metadata Refresh)**
```sql
MSCK REPAIR TABLE bitcoin_data;
```
- Scans the HDFS directory and updates Hive’s metastore with any new partitions.
- Essential after new data is loaded into partitioned paths externally (e.g., by Spark jobs or Kafka consumers).

---

### 🧾 Notes

- These commands assume Hive is connected to your metastore and has access to the HDFS path mentioned.
- Partitioning is crucial for efficient time-based queries and performance at scale.
- Always run `MSCK REPAIR TABLE` after adding new partitioned data files to HDFS.

---
