import os
from datetime import timedelta

from airflow import DAG
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
DATA_SPLIT_PATH = "/data/split/{{ ds }}"
DATA_TRANSFORMED_PATH = "/data/transformed/{{ ds }}"
MODEL_PATH = "/data/model/{{ ds }}"

with DAG(
    "train_pipeline",
    default_args=default_args,
    schedule_interval="@weekly",
    start_date=days_ago(30),
) as dag:
    split = DockerOperator(
        image="airflow-split",
        command=f"-l {DATA_RAW_PATH} -s {DATA_SPLIT_PATH}",
        network_mode="bridge",
        task_id="split",
        do_xcom_push=False,
        auto_remove=True,
        volumes=[f"{HOST_DATA_DIR}:/data"],
    )

    fit_transformer = DockerOperator(
        image="airflow-fit-transformer",
        command=f"-l {DATA_SPLIT_PATH} -s {DATA_TRANSFORMED_PATH} -m {MODEL_PATH}",
        network_mode="bridge",
        task_id="fit_transformer",
        do_xcom_push=False,
        auto_remove=True,
        volumes=[f"{HOST_DATA_DIR}:/data"],
    )

    fit_model = DockerOperator(
        image="airflow-fit-model",
        command=f"-d {DATA_TRANSFORMED_PATH} -m {MODEL_PATH}",
        network_mode="bridge",
        task_id="fit_model",
        do_xcom_push=False,
        auto_remove=True,
        volumes=[f"{HOST_DATA_DIR}:/data"],
    )

    validate = DockerOperator(
        image="airflow-validate",
        command=f"-d {DATA_TRANSFORMED_PATH} -m {MODEL_PATH}",
        network_mode="bridge",
        task_id="validate",
        do_xcom_push=False,
        auto_remove=True,
        volumes=[f"{HOST_DATA_DIR}:/data"],
    )

    split >> fit_transformer >> fit_model >> validate
