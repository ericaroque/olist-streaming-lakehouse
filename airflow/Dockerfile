FROM apache/airflow:3.1.7-python3.12

RUN pip install --no-cache-dir "apache-airflow==3.1.7" \
    "apache-airflow-providers-databricks==7.9.0" \
    --constraint "${HOME}/constraints.txt"