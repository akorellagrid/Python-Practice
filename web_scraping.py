import requests
from bs4 import BeautifulSoup

response = requests.get('https://portfolio-3-0-beta-eight.vercel.app/')

soup = BeautifulSoup(response.text, 'lxml')

content = soup.select('div.portfolio-item-title')[0].get_text()

print(content)