from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum

def print_execution_date(date):
    print(date)

with DAG(
        'templating_example',
        start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
        schedule_interval='@monthly',
        catchup=False

) as dag:

    print_execution_date_task = PythonOperator(
        task_id="print_execution_date",
        python_callable=print_execution_date,
        op_kwargs=dict(date="{{ ds }}")
    )

    print_execution_date_task
