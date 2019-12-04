import requests
from bs4 import BeautifulSoup


URL = 'https://www.amazon.in/dp/B07HG8SBDW/ref=twister_B07WBTR89J'

headers = {"User Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle")

price = soup.find(id="priceblock_ourprice")
price = price.text.strip()
price = price[2:]
ogprice = float(price.replace(",",""))

print(title.text.strip())
print(ogprice)
