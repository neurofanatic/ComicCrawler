#| IMPORTS |-----------------------------------------------------------------------------------------
import urllib.request 
from bs4 import BeautifulSoup 
import re
import os
# import regex_code as regex

#| VARIABLES |---------------------------------------------------------------------------------------
URL = 'https://manganelo.com/manga/tales_of_demons_and_gods'
chapter_list = []
image_list = []

#| DATA COLLECTION |---------------------------------------------------------------------------------
def getdata_dict (a):
    matches = re.search('title=\"(.+)chapter ([\d\.\s\w]+)(?:\s?: (.+))?\">', a)
    title = matches.group(1)
    chapter = matches.group(2)
    chapter_name = matches.group(3)
    return {'title': title, 'chapter': chapter, 'chapter_name': chapter_name}

#| ZUGRIFF WEBSITE URL |-----------------------------------------------------------------------------
def html_request(url):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,}
    request = urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    soup = BeautifulSoup(data, 'lxml')
    return soup
    
#| ZUGRIFF CHAPTER URL |--------------------------------------------------------------------------------
for item in html_request(URL).select(".row a"):   
    link = item
    link = str(link).lower()
    data_dict = getdata_dict(link)
    chapter_list.append(item.get('href'))

#| ZUGRIFF IMAGE URL |---------------------------------------------------------------------------------
for item_a in chapter_list:
    for item_b in html_request(item_a).select("#vungdoc img"):
        image_list.append(item_b.get('src'))
       
# print(image_list)

#| DOWNLOAD IMAGES |-----------------------------------------------------------------------------------
def dwnld(url, path):
    for item in image_list:
        s = data_dict['title']
        re.search('%s ', item) % s
        filename = item.split('/')[-1]
        
        try: 
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)
    urllib.request.urlretrieve(url, path)


path = "C:\_CODING_\_testing_\\new\\bye\yes"

try: 
    os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s " % path)


