### 📂 Hadoop_Commands

This folder contains basic Hadoop Distributed File System (HDFS) commands used during the initial setup and management of HDFS directories as part of the larger data streaming and processing pipeline.

These commands were primarily used to:
- Create directories in HDFS
- Remove directories and their contents
- List contents of directories

---

### 📜 Commands Reference

1. **Creating a Directory in HDFS**
   ```bash
   hadoop fs -mkdir /trial
   ```
   - Creates a directory named `trial` in the root (`/`) of HDFS.

2. **Deleting a Directory in HDFS Recursively**
   ```bash
   hadoop fs -rm -r /trial
   ```
   - Deletes the `/trial` directory along with all its contents.
   - The `-r` flag ensures recursive deletion.

3. **Listing the Contents of a Directory**
   ```bash
   hadoop fs -ls /
   ```
   - Lists all files and folders in the root of the HDFS directory structure.

---

### 🧾 Notes

- These commands assume that Hadoop is properly installed and configured.
- Run these in your terminal or Hadoop shell environment.
- Use these cautiously, especially the `-rm -r` command, as it will permanently remove files/folders from HDFS.

---
