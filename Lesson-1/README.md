# 📘 Lesson 1: PySpark Basics

This lesson introduces the fundamentals of using PySpark in GitHub Codespaces. It walks through:

- Creating a Spark session
- Building a DataFrame
- Running basic DataFrame operations
- Writing and reading CSV files

---

## 🧱 Step-by-Step Guide

### ✅ Step 1: Create a SparkSession

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("BasicSparkApp") \
    .getOrCreate()
```

This initializes a Spark session, which is the entry point to use PySpark.

---

### ✅ Step 2: Create a DataFrame

```python
data = [
    (1, "Alice", 29),
    (2, "Bob", 31),
    (3, "Cathy", 27)
]

columns = ["id", "name", "age"]
df = spark.createDataFrame(data, columns)
df.show()
```

Creates an in-memory DataFrame with 3 rows and displays it.

---

### 🧪 Step 3: DataFrame Operations

#### 3.1 Print Schema

```python
df.printSchema()
```

Shows the structure and data types of the DataFrame.

#### 3.2 Select Columns

```python
df.select("name").show()
```

Selects and displays only the `name` column.

#### 3.3 Filter Rows

```python
df.filter(df.age > 28).show()
```

Filters the rows to show only those with `age > 28`.

#### 3.4 Add New Column

```python
from pyspark.sql.functions import col
df.withColumn("age_plus_5", col("age") + 5).show()
```

Adds a derived column called `age_plus_5`.

---

## 💾 Step 4: Write and Read CSV

### ✅ Write as Single CSV

```python
df.coalesce(1).write.mode("overwrite").csv("Lesson-1/output/output.csv", header=True)
```

- `coalesce(1)` ensures only one part file is written.
- Output is saved in the `Lesson-1/output/output.csv/` folder.

### ✅ Read Back CSV

```python
df2 = spark.read.csv("Lesson-1/output/output.csv", header=True, inferSchema=True)
df2.show()
```

Reads the CSV back into a new DataFrame and displays it.

---

## 📁 Output

The output directory contains:

```
Lesson-1/output/output.csv/
├── part-00000-xxxx.csv   <-- actual data
└── _SUCCESS              <-- Spark job success marker
```

---

## 🧼 Notes

- Use `.coalesce(1)` to simplify file outputs when working locally.
- Do not open the `output.csv` folder expecting a `.csv` file directly — Spark writes partitioned output.

---
