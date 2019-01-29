#!/usr/bin/python3.7
"""
file: yt.py
Author: github.com/eatDatCode
"""
import sys
import re

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
        length = durations[i].get_text()[3:]
        href = ancors[i].get('href')
        
        if '&list' in href:
            href = re.sub('.*&list','list',href)
            link = 'https://www.youtube.com/playlist?'+href
        else:
            link = 'https://www.youtube.com' + href

        result = "[%2d] %s || %s || %s " % (i+1,title,length,link)
        print(result)
        print('-'*len(result))

def get_user(query):
    """Take the input channel name and find the associate youtube username."""

    html = requests.get(query).text
    soup = BeautifulSoup(html,'lxml')
    links = soup.select('div .yt-lockup-content')
    
    count = 0
    channel = {}
    for i in range(len(links)):
        user = links[i].find('a',{'class':'yt-uix-tile-link'})
        title = user.get('title')
        url = user.get('href')
        desc = links[i].find('div',{'class':'yt-lockup-description'})
        details = "No details available"

        if '/watch?v=' not in url: 
            count += 1
            channel[count]= url
            if desc:
                details = desc.get_text()

            results = '[%2d] %s || %s' % (count ,title ,details)
            print(results)
            print('-'*len(results))
    
    if count == 0:
        youtube(query)

    elif count == 1:
        href = 'https://www.youtube.com' + channel[1] + '/playlists'
        get_playlists(href)

    else:
        while True:
            try:
                choice = int(input('Which channel? :'))
                break
            except ValueError:
                print("Enter the choice number![--]")

        href = 'https://www.youtube.com' + channel[choice] + '/playlists'
        get_playlists(href)


def get_playlists(query):
    """ Lists at least 30 playlis of the channel """

    html = requests.get(query).text
    soup = BeautifulSoup(html,'lxml')
    playlists = soup.findAll('a',{'class':'yt-uix-tile-link'})

    for i in range(len(playlists)):
        title = playlists[i].get('title')
        href = 'https://www.youtube.com' + playlists[i].get('href')
        result = "[%2d] %s || %s " % (i+1,title,href)
        print(result)
        print('-'*len(result))

if __name__=='__main__':
    if len(sys.argv) < 2:
        print('Enter the search query!')
        exit()

    query = 'https://www.youtube.com/results?search_query=' + '+'.join(sys.argv[1:])

    if sys.argv[len(sys.argv)-1]=='channel':
        get_user(query)

    else:
        youtube(query)
