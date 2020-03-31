# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:49:35 2020

@author: Terentak

cheatsheet: https://www.banjocode.com/web-scraping/

"""

from bs4 import BeautifulSoup
import requests
import re
import os
from download_images import download_images, slugify, non_alpha

chapter_urls = []
data_list = []
URL = input ("type the URL here: " )

result = requests.get(URL)
content = result.content
soup = BeautifulSoup(content, features="lxml")

a_tag_list = soup.find_all("a", "chapter-name text-nowrap")


def getdata_dict(a_tag):
    matches = re.search('title=\"(.+)chapter ([\d\.\s\w]+)(?:\s?: (.+))?\">', a_tag)
    title = str(matches.group(1)).strip()
    chapter = non_alpha(str(matches.group(2)))
    chapter_name = str(matches.group(3))
    return {'title': title, 'chapter': chapter, 'chapter_name': chapter_name}

"""-------------------------- append data_list -----------------------------"""
for a_tag in a_tag_list:
    data_list.append(getdata_dict(str(a_tag)))
    chapter_urls.append(a_tag.get('href'))
  
index=1

filename = slugify(data_list[0]["title"])

os.chdir('E:\\newPC\\comics')

if not os.path.exists(filename):
    os.mkdir(filename)
    print("made dor: " + filename)
    os.chdir(filename)
    print("moved to dir: " + filename)
else: 
    os.chdir(filename)
    print("moved to dir2: " + filename)

        
chapter_urls.reverse()

for chapter_url in chapter_urls:
    chapterfile = slugify('Chapter_' + str(data_list[-index]["chapter"]) + '-' + str(data_list[-index]["chapter_name"]))
    try:
        if not os.path.exists(chapterfile):
            os.mkdir(chapterfile)
            print("made dir: " + chapterfile)
            os.chdir(chapterfile)
            download_images(chapter_url)
            print("downloaded image")
            os.chdir("..")
            
    except OSError:
        print("Creation of the chapter directory failed")
        
    index+=1