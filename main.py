from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
article_tag = soup.find('span', class_='titleline')
article_title = article_tag.find('a')
print(article_title.get_text())

