#merge file
import pandas as pd
df1 = pd.read_csv("/Users/kk/Desktop/py/film_1.csv")
df2 = pd.read_csv("/Users/kk/Desktop/py/film_2.csv")
merged_df = pd.merge(df1, df2, on = "id")
merged_df.to_csv('films.csv', index= False)
