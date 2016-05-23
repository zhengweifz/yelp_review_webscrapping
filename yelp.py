# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:48:48 2015

@author: weizheng
"""

import requests as rq
from bs4 import BeautifulSoup
import pandas as pd


basic_link = "http://www.yelp.com/search?find_desc=Restaurants&find_loc=Washington,+DC&start="
all_links = [basic_link + str(x * 10) for x in xrange(100)]

restaurants = []

for link in all_links:
    response=rq.get(link)
    soup = BeautifulSoup(response.text)
    divs = soup.findAll("div", {"class":"search-result natural-search-result"})
    for div in divs:
        a = div.find("a", {"class":"biz-name"})
        name = a.span.text
        rating_div = div.find('div', {"class":"rating-large"})
        rating_title = rating_div.i.attrs['title']
        rating = float(rating_title.split(" ")[0])
        address_div = div.find('div', {"class": "secondary-attributes"})
        address = address_div.address.text.strip()
        restaurants.append((name, rating, address))

res_df = pd.DataFrame(restaurants, columns=["name", "rating", "address"])