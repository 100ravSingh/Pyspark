FROM mcr.microsoft.com/devcontainers/python:3.11

# Install Java (needed for Spark)
RUN apt-get update && apt-get install -y default-jdk

# Dynamically set JAVA_HOME
RUN echo "JAVA_HOME=$(dirname $(dirname $(readlink -f $(which javac))))" >> /etc/environment
ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH="$JAVA_HOME/bin:$PATH"

# Install PySpark
RUN pip install pyspark
