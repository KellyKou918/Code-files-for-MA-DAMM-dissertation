#delete columns
import pandas as pd
df1 = pd.read_csv("/Users/kk/Desktop/archive/films1.csv")
df2 = pd.read_csv("/Users/kk/Desktop/archive/films2.csv")
df1 = df1.drop(['reviewId','criticName','isTopCritic', 'originalScore', 'reviewState', 'reviewUrl'], axis = 1)
df2 = df2.drop(['audienceScore', 'tomatoMeter', 'rating', 'ratingContents', 'releaseDateTheaters', 'releaseDateStreaming', 'director', 'writer', 'boxOffice', 'distributor', 'soundMix'], axis = 1)
df1.to_csv('film_1.csv', index= False)
df2.to_csv('film_2.csv', index= False)
