FROM mcr.microsoft.com/devcontainers/python:3.11

# Install Java (needed for Spark)
RUN apt-get update && apt-get install -y openjdk-11-jdk

# Set JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

# Install PySpark
RUN pip install pyspark
