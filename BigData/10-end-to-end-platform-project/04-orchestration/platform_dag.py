"""Airflow ortamına taşınabilecek platform DAG taslağı."""
from __future__ import annotations
from airflow.decorators import dag,task
from pendulum import datetime
@dag(schedule="@daily",start_date=datetime(2026,1,1,tz="UTC"),catchup=False,tags=["platform"])
def platform_pipeline():
 @task
 def ingest():return "bronze/events"
 @task
 def quality(path):return path
 @task
 def transform(path):print(f"Silver/Gold dönüşümü: {path}")
 transform(quality(ingest()))
platform_pipeline()
