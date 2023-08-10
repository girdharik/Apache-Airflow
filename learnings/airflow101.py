#import the required libraries
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators import BashOperator


#defining the default arguments dictionary
args = {
    'owner': 'airflow'
    'start_date': 'datetime(2023,08,10)'
    'retries': 1
    "retry_delay": timedelta(seconds=10),
}

dag = DAG('sample', default_args=args)

#task1 is to create a directory 'test_dir' inside the dags folder
task1 = BashOperator(task_id='create_directory',
                     bash_command='mkdir ~/dags/test_dir', dag=dag)

#task2 is to get the 'shasum' of 'test_dir' directory
task2 = BashOperator(task_id='get_shasum',
                     bash_command='shasum ~/dags/test_dir', dag=dag)

#defining relationship
task1 >> task2