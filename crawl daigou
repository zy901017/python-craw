import requests
url='http://www.ausomg.com/goods/search.htm?categoryId=2'
infor=requests.get(url).text
from bs4 import BeautifulSoup #解析数据
soup=BeautifulSoup(infor,'lxml') #运用lxml 解析工具解析infor 数据形成SOUP
key=soup.find_all('span','imp') #在解析出来的SOUP中提取 html标签名为'span' 与class属性为'imp'的数据---产品名字形成list
key2=soup.find_all('span','pri') #----------html标签名为'span'与class属性为'pri'的数据--产品价格形成list
names=[] #空列表用于存储产品名字
for name in key: #遍历产品名字list
    names.append(name.string) #name.string 意思是什么意思？？？？
print(names)
prices=[]
for price in key2:
    prices.append(price.string)
print(prices)
#连个list 合并到dictionary中
keys=names
values=prices
product_details=dict(zip(keys,values))
print(product_details)

# 读取数据存入数据库中

import pandas



#再次爬取价格
#使用字典组合生成 产品名字：价格组合
