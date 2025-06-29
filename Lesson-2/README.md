# 📘 Lesson 2: Aggregations and GroupBy in PySpark

This lesson builds on the basics from Lesson 1. It introduces how to summarize and analyze data using `groupBy()` and aggregation functions in PySpark.

We also demonstrate saving both the original and transformed DataFrames to CSV files using `.coalesce(1)`.

---

## ✅ Step-by-Step Code Breakdown

### 🔹 Step 1: Start Spark Session

```python
spark = SparkSession.builder.appName("Lesson2-Aggregations").getOrCreate()
```

Initializes Spark.

---

### 🔹 Step 2: Create a Sample DataFrame

```python
data = [
    ("Electronics", "Laptop", 1200),
    ...
]
df = spark.createDataFrame(data, ["category", "product", "price"])
df.show()
```

Creates a DataFrame with product category, name, and price.

---

### 💾 Save Original DataFrame

```python
df.coalesce(1).write.mode("overwrite").csv("Lesson-2/output/original_data.csv", header=True)
```

Saves the original data as a single CSV file in `output/original_data.csv`.

---

### 🔹 Step 3: Count Products per Category

```python
df.groupBy("category").count().show()
```

Shows how many products belong to each category.

---

### 🔹 Step 4: Aggregate Price Stats

```python
df.groupBy("category").agg(
    avg("price"), sum("price"), max("price"), min("price")
).show()
```

Shows average, total, highest, and lowest prices for each category.

---

### 💾 Save Aggregated Category Stats

```python
agg_df.coalesce(1).write.mode("overwrite").csv("Lesson-2/output/category_aggregations.csv", header=True)
```

Saves aggregated stats per category.

---

### 🔹 Step 5: Group by Multiple Columns

```python
df.groupBy("category", "product").agg(
    count("*"), avg("price")
).show()
```

Groups by both `category` and `product` to get finer-grained stats.

---

### 💾 Save Product-Level Summary

```python
multi_df.coalesce(1).write.mode("overwrite").csv("Lesson-2/output/category_product_summary.csv", header=True)
```

Stores multi-level aggregation result in CSV format.

---

## 📁 Output Folder Structure

```
Lesson-2/output/
├── original_data.csv/
├── category_aggregations.csv/
└── category_product_summary.csv/
```

Each folder contains:
- A single CSV file (e.g. `part-00000-*.csv`)
- A `_SUCCESS` file (written automatically by Spark)

---

## ✅ Key Learnings

- Use `.groupBy().agg()` to perform multi-column aggregations.
- Use `.alias()` to rename result columns.
- Save output with `.coalesce(1)` to avoid multiple part-files.
- Spark always writes output as directories (not single files).

---

## ▶️ To Run

From Codespace terminal:

```bash
python Lesson-2/main.py
```

---

## 🧭 Next Up

Lesson 3 will cover:
- Joins between DataFrames
- Data enrichment using multiple datasets
- Realistic CSV data

---
