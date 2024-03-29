import pandas as pd
import argparse
from sqlalchemy import create_engine
from time import time

df = pd.read_csv('yellow_tripdata_2021-01.csv', nrows=100)

df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)


engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine)
chunk = 1
df_iter = pd.read_csv('yellow_tripdata_2021-01.csv', iterator=True, chunksize=100000)
df = next(df_iter)
df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
df.to_sql(name='yellow_taxi_data', con=engine,if_exists='append')

while True:
    t_start = time()
    chunk+=1
    df = next(df_iter)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')
    t_finish = time()
    print(f'chunk {chunk} inserted, it took %.3f second'%(t_finish-t_start))