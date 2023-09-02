import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
test_data_with_predictions = pd.read_csv("test_data_with_predictions.csv")

# Convert 'creationDate' column to datetime format
test_data_with_predictions['creationDate'] = pd.to_datetime(test_data_with_predictions['creationDate'], format='%Y-%m-%d')

# Set start date to 2000
start_date = pd.to_datetime('2000-01-01')
end_date = pd.to_datetime('2022-12-31')

filtered_data = test_data_with_predictions[(test_data_with_predictions['creationDate'] >= start_date) & (test_data_with_predictions['creationDate'] <= end_date)].copy()
filtered_data['year'] = filtered_data['creationDate'].dt.year


# Get the top 5 genres for each year
top_genres_by_year = filtered_data.groupby('year')['genre'].value_counts().groupby(level=0, group_keys=False).nlargest(5)

# Reset index for better visualization
top_genres_by_year = top_genres_by_year.reset_index(name='count')

# Create a bubble plot for each year's top 5 genres
plt.figure(figsize=(10, 6))  # Adjust figure size
colors = sns.color_palette("Blues", n_colors=len(top_genres_by_year['genre'].unique()))
sns.scatterplot(x='year', y='genre', size='count', data=top_genres_by_year, sizes=(50, 500), hue='genre', palette=colors, legend=False)
plt.title("Top 5 Genres Each Year (2000-2022) - Bubble Plot")
plt.xlabel("Year")
plt.ylabel("Genre")
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility

# Adjust subplot layout to show x-axis labels completely
plt.subplots_adjust(bottom=0.3)  # Adjust bottom margin

# Set y-axis ticks and labels using genre values
plt.yticks(top_genres_by_year['genre'].unique())

plt.tight_layout()
plt.show()
