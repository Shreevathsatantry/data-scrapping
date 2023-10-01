import requests
from bs4 import BeautifulSoup

url="https://www.flipkart.com/search?q=chairs&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
HEADERS=({"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Accept-Language':'en-US,en q=0.5'})
website=requests.get(url,headers=HEADERS)
print(website)
r=requests.get(url)
htmlcontent=r.content
# print(htmlcontent)
Soup=BeautifulSoup(htmlcontent,'html.parser')
# # print(Soup.prettify)
# title=Soup.title
# # print(title)
# paras=Soup.find_all('p',class_="zSYht7")
# print(paras)
# anchors=Soup.find_all('a')
# # print(anchors)
# # print(Soup.find_all('p').get_text())
# product=[]
# Rating=[]
# Price=[]
# for i in Soup.find_all('a',href=True,class_='_4ddWXP'):
    # title=(Soup.find('a',class_='s1Q9rs').get_text())
    # print(title)
    # price=(Soup.find('div',class_='_30jeq3').get_text())
    # print(price)
    # review=(Soup.find('div',class_='_3LWZlK').get_text())
    # print(review)
name= (Soup.find('a',class_='s1Q9rs').get_text())
price=(Soup.find('div',class_='_30jeq3').get_text())
rating=Soup.find('div',class_='_3LWZlK _1D-8OL')
    # product.append(name.text)
    # Price.append(price.text)
    # Rating.append(rating.text)
print(name)
print(price)



