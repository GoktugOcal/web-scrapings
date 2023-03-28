import pandas as pd
import numpy as np
import json

with open("data\movies_detailed.json","r",encoding="utf8") as f:
    data = json.loads(f.read())


df = pd.DataFrame(data)

df = df.replace("N/A",None)
df["imdbRating"] = df["imdbRating"].astype(np.float)
df["Metascore"] = df["Metascore"].astype(np.float)

df["Number of awards"] = df.awards.str.split(",").map(lambda x: len(x) if x else 0)

df = df[['movie_name', 'original_name', 'director', 'runtime', 'genre', 'Metascore', 'imdbRating', 'Number of awards','awards', 'description', 'section', 'movie_page_url']]

df.columns = ['Name', 'Org. Name', 'Director', 'Duration', 'Genre', 'Metascore', 'IMDB Rating', 'Number of awards', 'Awards', 'Description', 'Festival Section', 'URL']

df.to_csv("data/movies.csv",index=False)
df.to_excel("data/movies.xlsx",index=False)
