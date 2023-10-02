import requests
from bs4 import BeautifulSoup

url="https://www.flipkart.com/cameras/dslr-mirrorless/pr?sid=jek%2Cp31%2Ctrv&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p%5B%5D=facets.type%255B%255D%3DMirrorless&param=179&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJTaG9wIE5vdyEiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJUb3AgTWlycm9ybGVzcyBDYW1lcmFzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fSwiaGVyb1BpZCI6eyJzaW5nbGVWYWx1ZUF0dHJpYnV0ZSI6eyJrZXkiOiJoZXJvUGlkIiwiaW5mZXJlbmNlVHlwZSI6IlBJRCIsInZhbHVlIjoiRExMRzJYRENGQlhWVVpUSCIsInZhbHVlVHlwZSI6IlNJTkdMRV9WQUxVRUQifX19fX0%3D"
HEADERS=({"User-Agent":'','Accept-Language':'en-US,en q=0.5'})
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
name= Soup.find('img',class_='_396cs4')
price=(Soup.find('div',class_='_30jeq3').get_text())
rating=Soup.find('div',class_='_3LWZlK _1D-8OL')
    # product.append(name.text)
    # Price.append(price.text)
    # Rating.append(rating.text)
print(name)
print(price)



