import pandas as pd 
import json

csv_data = pd.read_csv('data.csv')
data = csv_data.to_json(orient='records')

with open('data.json','w') as outfile:
    json.dump(data,outfile)