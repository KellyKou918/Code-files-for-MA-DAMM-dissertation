#Load the libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelBinarizer
from sklearn.utils import shuffle
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from wordcloud import WordCloud,STOPWORDS
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize,sent_tokenize
from bs4 import BeautifulSoup
import spacy
import re,string,unicodedata
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.stem import LancasterStemmer,WordNetLemmatizer
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from textblob import TextBlob
from textblob import Word
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score



df = pd.read_csv('/Users/kk/Desktop/py/sample_data_with_polarity.csv')



# 假设你的 DataFrame 中有 'runtimeMinutes' 和 'Polarity_Score' 列
# df = ...

# 将 runtimeMinutes 转换为整数
df['runtimeMinutes'] = df['runtimeMinutes'].astype(int)

# 根据电影时长分组，计算每个区间内的平均极性得分
interval_size = 10  # 区间大小为 10 分钟
df['runtime_group'] = (df['runtimeMinutes'] // interval_size) * interval_size
grouped_data = df.groupby('runtime_group')['Polarity_Score'].mean()

# 创建一个 DataFrame 用于存储区间和平均情感极性得分
result_df = pd.DataFrame({'Runtime Interval': grouped_data.index, 'Average Polarity Score': grouped_data.values})

# 打印表格
print(result_df)



# 假设你的 DataFrame 中有 'runtimeMinutes' 和 'Polarity_Score' 列
# df = ...

# 将 runtimeMinutes 转换为整数
df['runtimeMinutes'] = df['runtimeMinutes'].astype(int)

# 根据电影时长分组，计算每个区间内的平均极性得分
interval_size = 10  # 区间大小为 10 分钟
df['runtime_group'] = (df['runtimeMinutes'] // interval_size) * interval_size
grouped_data = df.groupby('runtime_group')['Polarity_Score'].mean()

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(grouped_data.index, grouped_data.values, marker='o')
plt.title('Average Polarity Score by Runtime Interval')
plt.xlabel('Runtime Interval (minutes)')
plt.ylabel('Average Polarity Score')
plt.grid(True)
plt.show()
