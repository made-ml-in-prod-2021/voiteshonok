import os
from datetime import timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

HOST_DATA_DIR = os.environ["HOST_DATA_DIR"]
DATA_RAW_PATH = "/data/raw/{{ ds }}"
MODEL_PATH = Variable.get("predicting_model_path")
PREDICTIONS_PATH = "/data/predictions/{{ ds }}"

with DAG(
    "predict",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=days_ago(30),
) as dag:
    predict = DockerOperator(
        image="airflow-predict",
        command=f"-d {DATA_RAW_PATH} -m {MODEL_PATH} -p {PREDICTIONS_PATH}",
        network_mode="bridge",
        task_id="predict",
        do_xcom_push=False,
        auto_remove=True,
        volumes=[f"{HOST_DATA_DIR}:/data"],
    )

    predict
