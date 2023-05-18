from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    'bash_test',
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['bash']
) as dag:

    t = BashOperator(
        task_id='bash_test',
        bash_command='echo "Hello Avi..."',
        dag=dag,
        executor_config={
        "pod_template_file": "/usr/local/airflow/new-pod-template.yaml",
    },
    )

