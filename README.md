# ⚡ PySpark Tutorial

This project is a hands-on **PySpark tutorial** designed to run inside **GitHub Codespaces**. It helps you learn and practice PySpark by walking through real examples — from basic DataFrame operations to reading/writing files and setting up your development environment.

---

## 📘 Lessons

| Lesson | Description                                                                 |
|--------|-----------------------------------------------------------------------------|
| 1️⃣     | [Lesson 1](./Lesson-1/README.md) – PySpark Basics — SparkSession, DataFrame ops, CSV I/O |
| 2️⃣     | [Lesson 2](./Lesson-2/README.md) – Aggregations and GroupBy — summary stats, multi-level grouping, CSV output |

---

## 📘 What is PySpark?

**PySpark** is the Python API for [Apache Spark](https://spark.apache.org/), an open-source distributed computing framework used for big data processing and analytics.

It allows you to:

- Create and transform large-scale **distributed DataFrames**
- Run complex SQL-like queries using Python
- Handle data stored in formats like **CSV, JSON, Parquet**
- Scale computations across multiple cores or machines (even clusters)

---

## 🔁 How is PySpark Different from Standard Python?

| Feature                     | Standard Python (`pandas`, etc.) | PySpark                            |
|----------------------------|----------------------------------|------------------------------------|
| Data Size                  | In-memory only (limited by RAM)  | Distributed (handles huge datasets) |
| Execution                  | Single-threaded                  | Parallel, distributed              |
| Syntax                     | Pythonic                         | Similar to SQL + functional API   |
| Use Case                   | Small to mid-sized data          | Big Data, scalable analytics       |
| Performance                | Slower on large datasets         | Optimized with JVM + Spark engine |

---

## 🛠️ Environment Setup (via `.devcontainer`)

This project uses a **`.devcontainer`** configuration to set up:

- Python 3.11
- PySpark
- Java (via `default-jdk`)
- Jupyter + VS Code Python extensions

### Dev Container Includes:

- `Dockerfile` — builds the container with Java and PySpark installed
- `devcontainer.json` — VS Code Codespace settings
- `requirements.txt` — lists additional Python packages

---

## 🚀 Getting Started

1. **Open this repo in GitHub Codespaces**
2. The container auto-builds with Java and PySpark installed
3. To **verify installation**, run:

```bash
python -c "import pyspark; print(pyspark.__version__)"
```

To Run
```bash
python <filename>.py
```

---