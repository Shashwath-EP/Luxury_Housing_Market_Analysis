import pandas as pd
from sqlalchemy import create_engine

# load dataset
df = pd.read_csv("data/housing_data.csv")

# connect to database
engine = create_engine("mysql+pymysql://root:tron*19@localhost/housing_db")

# insert data
df.to_sql("luxury_housing", engine, if_exists="append", index=False)

print("Data uploaded successfully")