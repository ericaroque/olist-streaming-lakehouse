import pendulum

from airflow.sdk import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator

with DAG(
    dag_id="olist_pipeline",
    start_date=pendulum.datetime(2026, 11, 16, tz="America/Sao_Paulo"),
    schedule=None,
    max_active_runs=1,
) as dag:
    DatabricksRunNowOperator(
        task_id="executar_olist_job",
        databricks_conn_id="olist_databricks",
        job_id=215472736601212,
        wait_for_termination=True,
    )