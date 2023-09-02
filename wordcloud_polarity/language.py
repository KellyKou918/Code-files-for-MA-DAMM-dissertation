#Load the libraries
import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/kk/Desktop/py/test_data_with_predictions.csv')

positive_comments = data[data['predictedSentiment'] == 'Positive']

positive_counts = positive_comments.groupby('originalLanguage').size().reset_index(name='positiveCount')

# 将原始语言和其积极评论数转换为词典
language_positive_count = dict(zip(positive_counts['originalLanguage'], positive_counts['positiveCount']))

# 创建词云图
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(language_positive_count)

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
