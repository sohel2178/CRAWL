import pandas as pd 

df = pd.read_json("data2.json")

df.to_csv('data2.csv')