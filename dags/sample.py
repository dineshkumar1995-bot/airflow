
from datetime import timedelta

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.microsoft.winrm.hooks.winrm import WinRMHook
from airflow.providers.microsoft.winrm.operators.winrm import WinRMOperator
from airflow.utils.dates import days_ago

with DAG(
    dag_id='POC_winrm_parallel',
    schedule_interval='0 0 * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
    tags=['example'],
) as dag:

    cmd = 'ls -l'
    run_this_last = DummyOperator(task_id='run_this_last')

    winRMHook = WinRMHook(ssh_conn_id='ssh_POC1')

#    t1 = WinRMOperator(task_id="wintask1", command='Get-Service', winrm_hook=winRMHook)

    t2 = WinRMOperator(task_id="wintask2", command='echo welcom gavs', winrm_hook=winRMHook)

    t3 = WinRMOperator(task_id="wintask3", command='echo \'luke test\' ', winrm_hook=winRMHook)

    [ t2, t3] >> run_this_last


