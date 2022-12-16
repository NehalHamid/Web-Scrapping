import np as np
import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl.workbook import Workbook
from itertools import zip_longest

#url=requests.get('https://books.toscrape.com/')

Book_titles=[]
Prices=[]
In_stocks=[]
Product_discriptions=[]
Links=[]

pages = np.arange(1,51)
for page in pages:
    page = requests.get('https://books.toscrape.com/catalogue/page-'+str(page)+'.html')
    soup=BeautifulSoup(page.content,'html.parser')
    Book_title = soup.find_all('h3')
    for i in range(len(Book_title)):
        Book_titles.append(Book_title[i].find('a').attrs['title'])
        Links.append(Book_title[i].find('a').attrs['href'])

for link in Links:
    url='https://books.toscrape.com/catalogue/'+link
    page =requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    price=soup.find('p',{'class':'price_color'})
    In_stock=soup.find('p',{'class':'instock availability'})
    Product_discription=soup.find('p')
for In_Stock in In_stock:
    In_stocks.append(In_Stock.text)

#print(In_stocks)

#file_list ={Book_titles}
data=pd.DataFrame(Book_titles,In_stocks)
data.to_excel('python_Project.xlsx',index=False)


#ported =zip_longest(*file_list)

#with open("D:/THIRD YEAR/books/projects.csv","w") as myfile:
#    wr = csv.writer(myfile)
#    wr.writerow(["Book_titles","Book_prices","In_stock","Product_descriptions"])
#    wr.writerows(exported)

