import pandas as pd

# 读取CSV文件
data = pd.read_csv('/Users/kk/Desktop/py/films_new.csv')

# 根据标题提取包含关键词的reviewText
def print_reviews_with_keyword(title, keyword):
    movie_data = data[data['title'] == title]

    if not movie_data.empty:
        review_texts = movie_data['reviewText'].tolist()
        keyword_reviews = []

        for idx, review_text in enumerate(review_texts, start=1):
            if keyword in review_text:
                keyword_reviews.append((idx, review_text))

        if keyword_reviews:
            for idx, review_text in keyword_reviews:
                print(f"Review {idx}:\n{review_text}\n{'='*30}")
        else:
            print(f"No reviews containing the keyword found for the movie with title: {title}")
    else:
        print(f"No reviews found for the movie with title: {title}")

# 要查找的电影标题和关键词
movie_title = "Mirrors"
search_keyword = "unfeasibly"

print_reviews_with_keyword(movie_title, search_keyword)
