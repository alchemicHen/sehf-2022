# Import package
import pandas as pd
import numpy as np

# import from CSV
prices = pd.read_csv('price_mid_wkly.csv', index_col = 0, low_memory = False)

