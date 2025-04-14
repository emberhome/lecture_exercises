from airflow import DAG
import pendulum
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.sqlite_operator import SqliteOperator

def my_sleeping_function(time_to_sleep):
    import time
    time.sleep(time_to_sleep)

with DAG(
    'lewagon_example',
    description='A simple DAG for le wagon',
    schedule_interval='@daily',
    start_date=pendulum.datetime(2025, 1, 27, tz="UTC"),
    catchup=False
) as dag:
    run_this_last = EmptyOperator(
        task_id='run_this_last',
    )

    run_this_first = BashOperator(
        task_id='run_this_first',
        bash_command='echo 1',
    )

    for i in range(5):
        task = PythonOperator(
            task_id=f'run_this_{i}',
            python_callable=my_sleeping_function,
            op_kwargs={'time_to_sleep': i},
        )

        run_this_first >> task

    create_example_table_task = SqliteOperator(
    task_id="create_example_table",
    sql="CREATE TABLE examples (example VARCHAR);",
    sqlite_conn_id='sqlite_connection'
)

    run_this_first >> run_this_last >> create_example_table_task
