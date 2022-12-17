import csv
import np as np
import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook,load_workbook
from itertools import zip_longest

#url=requests.get('https://books.toscrape.com/')

Book_titles=[]
Prices=[]
In_stocks=[]
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
    Prices.append(price.text.replace('£',''))
    In_stocks.append(In_stock.text.strip())

wb = load_workbook("D:/THIRD YEAR/books/python_Project.xlsx")
sh= wb['Sheet']
sh.append(['Book title','Prices','In stock'])
sh.save("C:/Users/c.delivery for lap/PycharmProjects/WebScrapingProject/python_Project.xlsx")

for i in range(1000):
    sh.append([Book_titles(i),Prices(i),In_stocks(i)])
sh.save("D:/THIRD YEAR/books/python_Project.xlsx")


'''
stored_result=[]
for i in range(1000):
    temporary={
        "Book title": Book_titles[i],
        "Price": Prices[i],
        "In stock": In_stocks[i] }
    stored_result.append(temporary)

data=pd.DataFrame(Book_titles,Prices,In_stocks)
data.to_excel('python_Project.xlsx',index=False)
'''
#file_list ={Book_titles,Prices,In_stocks}
#exported =zip_longest(*file_list)

#with open("D:/THIRD YEAR/books/project.csv","w") as myfile:
#    wr = csv.writer(myfile)
#    wr.writerow(["Book_titles","Book_prices","In_stock","Product_descriptions"])
#    wr.writerows(exported)

