from airflow import DAG
from airflow.operators.python import PythonOperator

from airflow.hooks.sqlite_hook import SqliteHook
from airflow.operators.sqlite_operator import SqliteOperator
import pendulum


def list_tables():
    hook = SqliteHook(sqlite_conn_id='sqlite_connection')
    dags = hook.get_records("SELECT * FROM dag;")
    for dag in dags:
        print(dag)

with DAG(
        'connections_example',
        start_date=pendulum.datetime(2025, 4, 1, tz="UTC"),
        schedule_interval='@daily',
) as dag:

    list_tables_task = PythonOperator(
        task_id="list_tables",
        python_callable=list_tables,
    )

    list_tables_task
