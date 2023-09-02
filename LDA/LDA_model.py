import pandas as pd
import gensim
from gensim import corpora
from gensim.models import LdaModel
from nltk.corpus import stopwords
from sklearn.utils import shuffle
import string
from nltk.tokenize import word_tokenize

# 加载停用词
stop_words = set(stopwords.words('english'))

# 加载数据集
data = pd.read_csv("/Users/kk/Desktop/py/test_data_with_predictions.csv", low_memory=False)

# 随机选取3000行
num_samples = 3000
random_data = shuffle(data, random_state=42).head(num_samples)

def preprocess_text(text):
    if isinstance(text, str):  # 检查是否为字符串
        tokens = word_tokenize(text.lower())
        tokens = [token for token in tokens if token not in stop_words and token not in string.punctuation]
        return tokens
    else:
        return []  # 返回空列表，表示空文本

# 对 reviewText 进行预处理
random_data['cleaned_text'] = random_data['reviewText'].apply(preprocess_text)


# 构建词典
dictionary = corpora.Dictionary(random_data['cleaned_text'])

# 构建文档-词矩阵
corpus = [dictionary.doc2bow(text) for text in random_data['cleaned_text']]

# 训练 LDA 模型
num_topics = 5
lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)

# 输出每个主题的关键词
for topic in lda_model.print_topics():
    print(topic)

# 应用模型
def get_topics(text):
    text_bow = dictionary.doc2bow(preprocess_text(text))
    topics = lda_model[text_bow]
    return topics

# 添加主题列到随机数据集
random_data['LDA_Topics'] = random_data['reviewText'].apply(get_topics)

# 保存包含主题的新数据集
random_data.to_csv('random_data_with_lda_topics.csv', index=False)
