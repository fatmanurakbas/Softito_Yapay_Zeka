"""Airflow TaskFlow API ile örnek, idempotent günlük pipeline."""
from __future__ import annotations
from datetime import timedelta
from airflow.decorators import dag,task
from pendulum import datetime
@dag(schedule="@daily",start_date=datetime(2025,1,1,tz="UTC"),catchup=False,default_args={"retries":2,"retry_delay":timedelta(minutes=5)},tags=["bigdata","sales"])
def daily_sales_pipeline():
 @task
 def extract(logical_date:str)->list[dict]:return [{"date":logical_date,"amount":120},{"date":logical_date,"amount":80}]
 @task
 def transform(rows:list[dict])->dict:return {"row_count":len(rows),"total":sum(row["amount"] for row in rows)}
 @task
 def load(summary:dict)->None:print(f"Idempotent hedefe yaz: {summary}")
 load(transform(extract("{{ ds }}")))
daily_sales_pipeline()
