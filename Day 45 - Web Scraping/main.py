import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=URL).text

soup = BeautifulSoup(response, 'html.parser')
movies = soup.find_all(name="h3", class_="title")

# Get the list of top 100 movies
with open('movies.txt', "w", encoding="utf-8") as file:
    for i in range(1, len(movies)+1):
        title = movies[-i].getText()
        file.write(f'{title}\n')
