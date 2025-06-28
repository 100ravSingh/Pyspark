# Use Microsoft Python dev container base (already includes pip, curl, git, sudo, bash, etc.)
FROM mcr.microsoft.com/devcontainers/python:3.10

# Install Java (needed by Spark)
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get clean

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

# Install Spark
ENV SPARK_VERSION=3.5.1
ENV HADOOP_VERSION=3
ENV SPARK_HOME=/opt/spark
ENV PATH="$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH"

RUN curl -fsSL https://downloads.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
    | tar -xz -C /opt && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} $SPARK_HOME

# Install Python dependencies
RUN pip install --no-cache-dir pyspark notebook ipykernel
