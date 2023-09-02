import pandas as pd
import matplotlib.pyplot as plt

# 读取带有 creationDate 和 predictedSentiments 的文件
test_data_with_predictions = pd.read_csv('test_data_with_predictions.csv')

# 将 creationDate 列转换为日期格式
test_data_with_predictions['creationDate'] = pd.to_datetime(test_data_with_predictions['creationDate'], format='%Y-%m-%d')

# 设置起始日期为1940年
start_date = pd.to_datetime('2000-01-01')
end_date = pd.to_datetime('2022-12-31')

# 使用筛选条件过滤出起始日期以后的数据
filtered_data = test_data_with_predictions[(test_data_with_predictions['creationDate'] >= start_date) & (test_data_with_predictions['creationDate'] <= end_date)]

# 根据 creationDate 分组，计算每个时间段内积极评论和消极评论的数量
resampled_data = filtered_data.groupby(pd.Grouper(key='creationDate', freq='1Y'))['predictedSentiment'].value_counts().unstack().fillna(0)

# 绘制折线图
resampled_data.plot(kind='line', marker='o', markersize=3, linewidth=1, color=['lightcoral', 'lightskyblue'])
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Positive and Negative Comments Over Time')
plt.legend(['Negative', 'Positive'])
plt.show()
