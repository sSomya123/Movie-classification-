import pandas as pd
import numpy as np

files = pd.read_csv("movie_genre_classification_final.csv")

rating_lists = {}
titles = files['Title']

print("Available ratings: " , files['Content_Rating'].unique())

movies_rating = files[['Title','Rating','Content_Rating']]

rating = files['Content_Rating'].unique()

for rates in rating:
    rating_lists[rates] = movies_rating[movies_rating['Content_Rating'] == rates].sort_values(by='Rating', ascending=False)

for rate, df in rating_lists.items():
    print(f"\n--- {rate} ---")
    print(df.head(3))  # Print first 3 movies for each content rating

