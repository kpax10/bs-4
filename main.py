from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
article_tag = soup.find('span', class_='titleline')
article_title = article_tag.find('a')

# if article_tag:
article_link = article_title.get('href')
article_score = article_title.find_next(class_='score')
print(article_link)
print(article_score.text)


# print(article_title.get_text())

# print(article_title.get('href'))