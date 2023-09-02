import pandas as pd
import re
# 假设您的DataFrame名为data
# data = ...
data = pd.read_csv("/Users/kk/Desktop/py/LDA/random_data_with_lda_topics.csv", low_memory=False)

# 提取LDA_Topics里的主题号（去除权重）
pattern = r'\((\d+),'
data['LDA_Topics'] = data['LDA_Topics'].apply(lambda x: [int(match.group(1)) for match in re.finditer(pattern, x)])

# 将LDA Topics的列表拆分为多行
expanded_data = data.explode('LDA_Topics')

# 统计每个主题的出现次数
topic_counts = expanded_data['LDA_Topics'].value_counts().reset_index()
topic_counts.columns = ['LDA_Topics', 'Counts']
topic_counts = topic_counts.sort_values('LDA_Topics')

print(topic_counts)
