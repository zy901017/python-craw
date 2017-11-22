import requests
from lxml import etree
def main(path): #编写主函数用于提取数据
    url='http://www.ausomg.com/goods/search.htm?categoryId=2&propertys=P33=%E9%99%8D%E4%BD%8E%E8%A1%80%E5%8E%8B'
    r=requests.post(url).text
    s=etree.HTML(r)
    final=s.xpath(path)
    return final
#提取产品名，函数中变量path='/html/body/div[4]/ul/li/div[2]/div[1]/a/span/text()'
# #运用xpath解析第一页产品名；

product_name=main('/html/body/div[4]/ul/li/div[2]/div[1]/a/span/text()')
print(product_name)
#提取价格
product_price=main('/html/body/div[4]/ul/li/div[2]/div[2]/span[1]/text()')
print(product_price)
#存储数据---
#resource::http://blog.csdn.net/claroja/article/details/64439735
#生成列表
key_1=product_name #列表1-产品名
key_2=product_price#列表2-价格
#字典套嵌列表
dictionary={
    '产品名':key_1,
    '产品价格':key_2,
    }
import pandas
data=pandas.DataFrame(dictionary)
data.to_csv('dictionary.csv')

