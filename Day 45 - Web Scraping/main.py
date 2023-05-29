from bs4 import BeautifulSoup
import requests

hn_url = 'https://news.ycombinator.com/news'
news = requests.get(url=hn_url).text

soup = BeautifulSoup(news, 'html.parser')
article_tag = soup.find(name="span", class_="titleline").find(name="a")
score_tag = soup.find(name="span", class_="score")

article_text = article_tag.get_text()
article_link = article_tag.get("href")
article_upvote = score_tag.get_text()

print(article_text)
print(article_link)
print(article_upvote)
