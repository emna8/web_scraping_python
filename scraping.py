import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

myurl='https://www.newegg.com/global/ch/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+card&ignorear=0&N=-1&isNodeId=1'

uClient=ureq(myurl)
page_html=uClient.read()
uClient.close()
#html parser
page_soup=soup(page_html,"html.parser")
#grabs each product
containers=page_soup.findAll("div",{"class":"item-container"})

filename="products2.csv"
f=open(filename,"w")
headers="Brand , Product_name\n"
f.write(headers)
for container in containers :
    brand=container.div.div.a.img['title']
    title_container=container.findAll("a",{"class":"item-title"})
    product_name=title_container[0].text
    f.write(brand+ ',' + product_name.replace(',','|')+ "\n")

f.close()    