#!/usr/bin/python3.7

"""
file: yt.py
Author: github.com/eatDatCode
"""

import sys
import requests
from bs4 import BeautifulSoup

def youtube(query):
    """This method scraps the details of the query from youtube.com"""

    html = requests.get(query).text
    soup = BeautifulSoup(html,'lxml')
    ancors = soup.findAll('a',{'class':'yt-uix-tile-link'})
    durations = soup.findAll('span',{'class':'accessible-description'})

    for i in range(len(ancors)):
        title = ancors[i].get('title')
        href = ancors[i].get('href')
        length = durations[i].get_text()[3:]
        link = 'https://www.youtube.com' + href
        result = "[%2d] %s || %s || %s " % (i+1,title,length,link)
        print(result)
        print('-'*len(result))

if __name__=='__main__':
    if len(sys.argv) < 2:
        print('Enter the search query!')
        exit()
    query = 'https://www.youtube.com/results?search_query=' + '+'.join(sys.argv[1:])
    youtube(query)
