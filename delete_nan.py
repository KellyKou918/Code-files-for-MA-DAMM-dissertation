#delete nan
import pandas as pd
data = pd.read_csv('films.csv')
clean_data = data.dropna(axis = 0, how = 'any')
pd.set_option('display.max_columns', None)
print(clean_data.head(50))
