import requests
from pandas.io.json import json_normalize
import pandas as pd

url = "https://api.exchangerate-api.com/v4/latest/USD"
df = pd.read_json(url)
print(df)