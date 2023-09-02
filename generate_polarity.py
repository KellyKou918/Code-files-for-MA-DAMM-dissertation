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


balanced_data = pd.read_csv("/Users/kk/Desktop/py/test_data_with_predictions.csv", low_memory= False)

#shuffle the dataset randomly
balanced_data = shuffle(balanced_data, random_state=42)


from tqdm import tqdm  # 导入 tqdm

# 假设你有一个名为 balanced_data 的 DataFrame，其中包含了 reviewText 列
# balanced_data = ...

# 从数据集中随机抽取3000个样本
sample_size = 3000
sampled_data = balanced_data.sample(n=sample_size, random_state=42)

# 使用向量化操作计算情感极性
def calculate_sentiment(row):
    blob = TextBlob(row['reviewText'])
    return blob.sentiment.polarity

# 将情感极性添加为一个新的列
sampled_data['Polarity_Score'] = 0.0  # 先创建一个初始列
with tqdm(total=len(sampled_data)) as pbar:  # 使用 tqdm 包装循环
    for index, row in sampled_data.iterrows():
        sampled_data.at[index, 'Polarity_Score'] = calculate_sentiment(row)
        pbar.update(1)  # 更新进度条

# 将数据导出到一个新的文件
output_file = "/Users/kk/Desktop/py/sample_data_with_polarity.csv"
sampled_data.to_csv(output_file, index=False)

# 打印包含情感极性得分的 DataFrame
print(sampled_data.head(5))

# 将情感极性得分分为5个类别
def categorize_polarity(polarity):
    if polarity <= -0.5:
        return 'Very Negative'
    elif polarity <= -0.2:
        return 'Negative'
    elif polarity <= 0.1:
        return 'Neutral'
    elif polarity <= 0.5:
        return 'Positive'
    else:
        return 'Very Positive'

# 为 DataFrame 中的每个样本添加情感极性类别
sampled_data['Polarity_Category'] = sampled_data['Polarity_Score'].apply(categorize_polarity)

# 对情感极性类别进行排序
category_order = [
    'Very Negative', 'Negative', 'Neutral', 'Positive', 'Very Positive'
]

# 计算情感极性得分的最小值和最大值
min_polarity = sampled_data['Polarity_Score'].min()
max_polarity = sampled_data['Polarity_Score'].max()

print("Minimum Polarity Score:", min_polarity)
print("Maximum Polarity Score:", max_polarity)

# 计算每个情感极性类别的样本数量
category_counts = sampled_data['Polarity_Category'].value_counts()

# 计算每个情感极性类别的百分比
category_percentages = (category_counts / len(sampled_data)) * 100

# 绘制情感极性类别的直方图，包括百分比和具体数字
plt.figure(figsize=(8, 6))
ax = sns.countplot(x='Polarity_Category', data=sampled_data, palette='Blues', order=category_order)
plt.title('Distribution of Sentiment Polarity Categories')
plt.xlabel('Polarity Category')
plt.ylabel('Count')
plt.xticks(rotation=45)

# 在每个直方图内部添加百分比和具体数字标签
for i, category in enumerate(category_order):
    ax.text(i, category_counts[category] / 2, f"{category_counts[category]}\n{category_percentages[category]:.1f}%", ha='center', va='center', color='black')

plt.tight_layout()
plt.show()
