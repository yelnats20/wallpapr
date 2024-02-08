import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

BASE_URL = "https://wallpaperscraft.com/"
ua = UserAgent()

headers = {
   "User-Agent": ua.random,
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
   "Accept-Language": "en-US,en;q=0.5",
   "Accept-Encoding": "gzip, deflate",
   "Connection": "keep-alive",
   "Upgrade-Insecure-Requests": "1",
}


response = requests.get(BASE_URL, headers=headers).text

soup = BeautifulSoup(response, 'lxml')
container = soup.find_all('li', class_='wallpapers__item')
for data in container:
    image = data.find('img', class_='wallpapers__image')['src']
    print(image)

print(len(container))
