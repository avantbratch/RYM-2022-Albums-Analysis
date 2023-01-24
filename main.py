from bs4 import BeautifulSoup
import pandas as pd

# Rate Your Music is an online collaborative database of music releases and films.
# Users can catalog items, assign ratings in a five-star rating system and review them.
# In this python code I extract relevant information  from the html file of 2022's best 100 album page using beautifulsoup,
# and save it in csv file for later analysis with pandas.

with open("aoty_2022.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# Album and Artist Names
artist = []
albums = []

album_artist = soup.find_all("span", {"class": "ui_name_locale_original"})
all_albums = [album_artist.string for album_artist in album_artist]

for x, element in enumerate(all_albums):
    if x % 2 != 0 and x < 200:
        artist.append(element)
    elif x < 199:
        albums.append(element)

# Ratings
all_ratings = soup.find_all("span", {"class": "stat page_charts_section_charts_item_details_average_num"})
rating = [str(rating.text) for rating in all_ratings]
print(rating)

# Genres (Two lists)
p_genres = soup.find_all("div", class_="page_charts_section_charts_item_genres_primary")
primary_genres = [genre.text for genre in p_genres]

# Rating Number
rating_quantity = []

ratings_number = soup.find_all("span", class_="has_tip")

for i, rating in enumerate(ratings_number):
    if i % 2 == 0 and i < 107:
        rating_quantity.append(rating.text)

for i, rating in enumerate(ratings_number):
    if i % 2 != 0 and 106 < i < 198:
        rating_quantity.append(rating.text)

# Date
dates = soup.find_all("div", class_="page_charts_section_charts_item_date")
release_date = [date.text for date in dates]

df = pd.DataFrame({'artist': artist,
                   'album': albums,
                   'release_date': release_date,
                   'genres': primary_genres,
                   'rating': rating,
                   'rating_quantity': rating_quantity})

# Creating csv format file
df.to_csv('rym_data_2022.csv', index=True, encoding='utf-8')
