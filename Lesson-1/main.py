#Step 1: Start a Spark Session --> This is required to use any PySpark functionality.

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("BasicSparkApp") \
    .getOrCreate()

#Step 2: Create a DataFrame --> You can start with a simple in-memory list of tuples:

data = [
    (1, "Alice", 29),
    (2, "Bob", 31),
    (3, "Cathy", 27)
]

columns = ["id", "name", "age"]

df = spark.createDataFrame(data, columns)
print("Dataframe: ")
df.show()

#Step 3: Basic DataFrame Operations

#3.1: Schema
print("Schema: ")
df.printSchema()

#3.2: Select Columns
print("Column: ")
df.select("name").show()

#3.3: Filter Rows
print("Filter: ")
df.filter(df.age > 28).show()

#3.4: Add Column
print("Column added: ")
from pyspark.sql.functions import col

df.withColumn("age_plus_5", col("age") + 5).show()

# Save  ---> coalesce means cluster together
# df.write.mode("overwrite").csv("Lesson-1/output/output.csv", header=True)
df.coalesce(1).write.mode("overwrite").csv("Lesson-1/output/output.csv", header=True)

# Load
df2 = spark.read.csv("Lesson-1/output/output.csv", header=True, inferSchema=True)
print("Load data: ")
df2.show()

