# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:49:46 2019

@author: VINEET
"""

import requests as r
from bs4 import BeautifulSoup

game_name = input("Enter Game name: ")

url="https://store.steampowered.com/search/?term="+game_name

res=r.get(url)

soup = BeautifulSoup(res.content,"lxml")

colomn = soup.find_all("div", {"class": "responsive_search_name_combined"})

for i in colomn:
    title = i.div.span.text
    print('Title: ' + title )
    try:
        price = i.find('div',{'class' : 'col search_price responsive_secondrow'})
        price = price.text.strip()
        if price!='':
            print( 'Price: ' + price )
    except:
        price = i.find('div',{'class' : 'col search_price discounted responsive_secondrow'})
        price = price.text.strip().split('₹')[2]
        if price!='':
            print( 'Price: ₹' + price )
    try:
        discount = i.find('div',{'class' : 'col search_price_discount_combined responsive_secondrow'})
        discount = discount.span.text
        print( 'Discount' + discount )
    except:
        pass    
    print()
'''
#title = coloum[0].find('span',{'class' : 'title'})
title = coloum[0].div.span.text
price = coloum[0].find('div',{'class' : 'col search_price responsive_secondrow'})
price = price.text.strip()
try:
    discount = coloum[0].find('div',{'class' : 'col search_price_discount_combined responsive_secondrow'})
    discount = discount.span.text
except:
    pass
'''