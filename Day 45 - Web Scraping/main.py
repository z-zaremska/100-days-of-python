from bs4 import BeautifulSoup
import requests

hn_url = 'https://news.ycombinator.com/news'
news = requests.get(url=hn_url).text

soup = BeautifulSoup(news, 'html.parser')
articles = [article.find(name="a") for article in soup.find_all(name="span", class_="titleline")]
scores = soup.find_all(name="span", class_="score")

article_texts = [article.get_text() for article in articles]
article_links = [article.get("href") for article in articles]
article_scores = [int(score.get_text().split()[0]) for score in scores]

print(article_texts)
print(article_links)
print(article_scores)
