import requests
from bs4 import BeautifulSoup
url="https://www.amazon.in/s?k=laptop&crid=204K7HTAWGV10&sprefix=lap%2Caps%2C241&ref=nb_sb_ss_ts-doa-p_2_3"
HEADERS=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Accept-Language': 'en-US,en q=0.5'})
website=requests.get(url,headers=HEADERS)
print(website)
r=requests.get(url)
htmlcontent=r.content
Soup=BeautifulSoup(htmlcontent,'html.parser')
product=Soup.find('span',class_='a-price-whole')
print(product.text)
