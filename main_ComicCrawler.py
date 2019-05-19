#| IMPORTS |-----------------------------------------------------------------------------------------
import urllib.request 
from bs4 import BeautifulSoup 
import re
import os
# import regex_code as regex

#| VARIABLES |---------------------------------------------------------------------------------------
URL = 'https://manganelo.com/manga/tales_of_demons_and_gods'
chapter_urls = []
image_list = []
data_list = []

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
    headers = {'User-Agent':user_agent,}
    request = urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    soup = BeautifulSoup(data, 'lxml')
    return soup

#| ZUGRIFF CHAPTER URL |--------------------------------------------------------------------------------
for item in html_request(URL).select(".row a"):   
    low = item
    low = str(low).lower()
    data_list.append(getdata_dict(low))
    chapter_urls.append(item.get('href'))
    
#| ZUGRIFF IMAGE URL |---------------------------------------------------------------------------------
for item_a in chapter_urls:
    for item_b in html_request(item_a).select("#vungdoc img"):
        image_list.append(item_b.get('src'))
    data_list[0].update( {'img': image_list})
  
#| DOWNLOAD IMAGES |-----------------------------------------------------------------------------------
def dwnld(url):
    temp_t = data_list['title']
    path_p = 'C:\\ComicCrawler\\{}'

    try:
        if not os.path.exists(path_p.format(data_list['title'])):
            os.makedirs(path_p.format(data_list['title'])) 
    except OSError:
        print("Creation of the parent directory failed")

    os.chdir(path_p.format(data_list['title']))

    for item in url:
        temp_c = data_list['chapter']
        temp_n = data_list['chapter_name']
        temp_p =  os.getcwd()
        path_c = temp_p + '{}' + '{}'

        try:
            if not os.path.exists(path_c.format('\\Chapter_' + temp_c, '-' + temp_n)):
                os.mkdir(path_c.format('\\Chapter_' + temp_c, '-' + temp_n)) 
        except OSError:
            print("Creation of the chapter directory failed")
            
    #     filename = item.split('/')[-1]         
    #     re.search('%s ', item) % s
    #   urllib.request.urlretrieve(url, path)

dwnld(image_list)



