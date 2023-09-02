import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

test_data_with_predictions = pd.read_csv('test_data_with_predictions.csv')

# 假设您已经进行了数据预处理和筛选
# 将 creationDate 列转换为日期格式
test_data_with_predictions['creationDate'] = pd.to_datetime(test_data_with_predictions['creationDate'], format='%Y-%m-%d')

# 设置起始日期为2000年
start_date = pd.to_datetime('2000-01-01')
end_date = pd.to_datetime('2022-12-31')

# 使用筛选条件过滤出起始日期以后的数据
filtered_data = test_data_with_predictions[(test_data_with_predictions['creationDate'] >= start_date) & (test_data_with_predictions['creationDate'] <= end_date)].copy()

# Extract year from 'creationDate'
filtered_data['year'] = filtered_data['creationDate'].dt.year

# 按年份和流派分组并计算每组内的正面评价数量
grouped_data = filtered_data[filtered_data['predictedSentiment'] == 'Positive'].groupby(['year', 'genre'])['predictedSentiment'].size().reset_index(name='positive_count')

# 获取每年正面评价前5的流派
top5_genres_per_year = grouped_data.groupby('year').apply(lambda x: x.nlargest(5, 'positive_count')).reset_index(drop=True)

# 绘制气泡图
plt.figure(figsize=(12, 8))
for year, group in top5_genres_per_year.groupby('year'):
    plt.scatter(group['year'], group['genre'], s=group['positive_count']*2, label='', color = 'Lightblue', sizes=(100, 200))



plt.xlabel('Year')
plt.ylabel('Genre')
plt.title('Top 5 Positive Review Genres per Year')
plt.tight_layout()
plt.show()
