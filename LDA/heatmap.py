import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re

# 假设您的DataFrame名为data
# data = ...
data = pd.read_csv("/Users/kk/Desktop/py/LDA/random_data_with_lda_topics.csv", low_memory= False)

# 统计出现次数前10的genre
top_genres = data['genre'].value_counts().head(10).index.tolist()

# 提取LDA_Topics里的主题号（去除权重）
pattern = r'\((\d+),'
data['LDA_Topics'] = data['LDA_Topics'].apply(lambda x: [int(match.group(1)) for match in re.finditer(pattern, x)])

# 将LDA Topics的列表拆分为多行
expanded_data = data.explode('LDA_Topics')

# 筛选数据，只包含出现次数前10的genre
filtered_data = expanded_data[expanded_data['genre'].isin(top_genres)]

# 绘制热力图，x轴为genre，y轴为LDA_Topics，值为计数
pivot_table = pd.pivot_table(filtered_data, index='genre', columns='LDA_Topics', aggfunc='size', fill_value=0)

# 设置颜色
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt='d')  # 添加 annot=True 和 fmt='d' 参数
plt.title('LDA Topics Distribution for Top 10 Genres')
plt.xlabel('LDA Topics')
plt.ylabel('Genre')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
