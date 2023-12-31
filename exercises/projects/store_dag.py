from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datacleaner import data_cleaner

from airflow.providers.mysql.operators.mysql import MySqlOperator


default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2023,8,12),
    'retries': 1,
    'retry_delay': timedelta(seconds=5 )
}

dag = DAG('store_dag', default_args=default_args, schedule_interval='@daily', catchup=False)

t1 = BashOperator(
    task_id='check_files_exists',
    bash_command='shasum gs://airflow_learning_projects/raw_store_transactions.csv',
    retries=2,
    retry_delay=timedelta(seconds=15),
    dag=dag
)

t2 = PythonOperator(
    task_id='clean_raw_csv',
    python_callable=data_cleaner,
    dag=dag
)

t3 = MySqlOperator(
    task_id='create_mysql_table',
    mysql_conn_id='mysql_conn',
    sql=
)