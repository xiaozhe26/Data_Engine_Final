#Project A 15963 Xiao Zhe

import pandas as pd
import requests
from bs4 import BeautifulSoup

# 得到页面的内容
def get_page_content (request_url):

    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html=requests.get(request_url,headers=headers,timeout=10)
    content = html.text
#    print(content)
    
    # 通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
#    print(soup)
    return soup

# 找到完整的车型信息
def analysis(soup):
    data_list = soup.find('div',class_="search-result-list")
    # 创建DataFrame
    df1 = pd.DataFrame(columns = ['car_name'])
    df2 = pd.DataFrame(columns = [ 'low_price','high_price'])
    df3 = pd.DataFrame(columns = [ 'picture_address'])
    temp1 = {}
    temp2 = {}
    temp3 = {}
    image_list = data_list.find_all('img',class_="img")
    name_list = data_list.find_all('p',class_="cx-name text-hover")
    price_list = data_list.find_all('p',class_="cx-price")
    for img in image_list:
        picture_address = img.get('src') 
        temp1['picture_address'] = picture_address
        df3 = df3.append(temp1,ignore_index = True )
        print(picture_address)
    for name in name_list:
        car_name = name.text
        temp2['car_name'] = car_name
        df1 = df1.append(temp2,ignore_index = True )
        print(car_name)
    for price_bt in price_list:
        price = price_bt.text
        temp3['low_price'] = price[0:4]
        temp3['high_price'] = price[6:10]
        df2 = df2.append(temp3,ignore_index = True )
        print(price)
    df = df1.join(df3.join(df2))

    return df

request_url = 'http://car.bitauto.com/xuanchegongju/?l=8&mid=8'
soup = get_page_content (request_url)
df = analysis (soup)

#导出数据
df.to_csv('project1_result.csv',encoding='gbk')


