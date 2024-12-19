import requests
from bs4 import BeautifulSoup


url = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all("h2")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
        