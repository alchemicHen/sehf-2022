# Import package
import pandas as pd
import numpy as np
import datetime as datetime

# import from CSV
prices_df = pd.read_excel('USO_Historical_Data_30_Minute.xlsx', sheet_name = "Jan 2012", index_col=False)
# print(prices_df.info())

date_df = prices_df[prices_df['Close'].isna()]

open_df = prices_df[prices_df['Time Interval'] == "09:30 - 10:00"]
close_df = prices_df[prices_df['Time Interval'] == "15:30 - 16:00"]

close_df['date'] = date_df['Time Interval']
open_df['date'] = date_df['Time Interval']

openclose_df = open_df.merge(close_df, on='date', how='left')
print(openclose_df.tail())

