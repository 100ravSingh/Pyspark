from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, sum, count, max, min

# 🔹 Step 1: Start Spark session
spark = SparkSession.builder.appName("Lesson2-Aggregations").getOrCreate()

# 🔹 Step 2: Sample data
data = [
    ("Electronics", "Laptop", 1200),
    ("Electronics", "TV", 800),
    ("Electronics", "Laptop", 1500),
    ("Clothing", "Shirt", 40),
    ("Clothing", "Jeans", 60),
    ("Clothing", "Shirt", 35),
    ("Groceries", "Apples", 5),
    ("Groceries", "Milk", 3),
    ("Groceries", "Apples", 6)
]

columns = ["category", "product", "price"]

df = spark.createDataFrame(data, columns)

print("🧾 Original Data:")
df.show()

# Save original data
df.coalesce(1).write.mode("overwrite").csv("Lesson-2/output/original_data.csv", header=True)

# 🔹 Step 3: Count products per category
print("🧮 Product count per category:")
count_df = df.groupBy("category").count()
count_df.show()

# Save the count data
count_df.coalesce(1).write.mode("overwrite").csv("Lesson-2/output/count_data.csv", header=True)

# 🔹 Step 4: Aggregate price stats per category
print("📊 Price stats per category:")
agg_df = df.groupBy("category").agg(
    avg("price").alias("avg_price"),
    sum("price").alias("total_price"),
    max("price").alias("max_price"),
    min("price").alias("min_price")
)
agg_df.show()

# Save aggregated data
agg_df.coalesce(1).write.mode("overwrite").csv("Lesson-2/output/category_aggregations.csv", header=True)


# 🔹 Step 5: Group by category and product
print("📦 Product count by category & product:")
multi_df = df.groupBy("category", "product").agg(
    count("*").alias("count"),
    avg("price").alias("avg_price")
)
multi_df.show()

# Save multi-level aggregation
multi_df.coalesce(1).write.mode("overwrite").csv("Lesson-2/output/category_product_summary.csv", header=True)