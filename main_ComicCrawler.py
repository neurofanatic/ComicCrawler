#-----------------------------------------------------------------------------------------| IMPORTS |
import urllib.request 
from bs4 import BeautifulSoup 
import re
import os
import requests

#---------------------------------------------------------------------------------------| VARIABLES |
URL = 'https://manganelo.com/manga/ch919349'
#URL =  input("Enter the Url of the Comic you want to downlaod: ")
chapter_urls = []
image_list = []
data_list = []
index = 0

#---------------------------------------------------------------------------------| DATA COLLECTION |
def getdata_dict (a):
    matches = re.search('title=\"(.+)chapter ([\d\.\s\w]+)(?:\s?: (.+))?\">', a)
    title = matches.group(1)
    chapter = matches.group(2)
    chapter_name = matches.group(3)
    return {'title': title, 'chapter': chapter, 'chapter_name': chapter_name}

#------------------------------------------------------------------------------| ACCESS WEBSITE URL |
def html_request(url):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent':user_agent,}
    request = urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    soup = BeautifulSoup(data, 'lxml')
    return soup

# ------------------------------------------------------------------------------| DIRECTORY CREATION |
def dwnld(data):
    
    index = 0
    t_title = data[index]['title']
    t_path =  os.getcwd()
    path_p = 'C:\\ComicCrawler\\{}'
    
    try:
        if not os.path.exists(path_p.format(t_title)):
            os.makedirs(path_p.format(t_title)) 
    except OSError:
        print("Creation of the parent directory failed")

    os.chdir(path_p.format(t_title))

    for item in data[index]['img']:
        t_chapter = data[index]['chapter']
        t_chapter_name = data[index]['chapter_name']
        path_c = t_path + '{}' + '{}'

        try:
            if not os.path.exists(path_c.format('\\Chapter_' + t_chapter, '-' + t_chapter_name)):
                os.mkdir(path_c.format('\\Chapter_' + t_chapter, '-' + t_chapter_name)) 
            else:
                os.chdir(path_c.format('\\Chapter_' + t_chapter, '-' + t_chapter_name))
        except OSError:
            print("Creation of the chapter directory failed")
        
        os.chdir(path_c.format('\\Chapter_' + t_chapter, '-' + t_chapter_name))
        
        img_name = path_c.format('\\Chapter_' + t_chapter, '-' + t_chapter_name)

        #----------------------------------------------------------------------------| IMAGE REQUEST |
        # filename = item.split('/')[-1] 
        img =requests.get(image_list[index]).content
        with open(img_name + ".png", 'wb') as handler:
            handler.write(img)

        # urllib.request.urlretrieve(item, path_c) !! SERVER_ERROR 403 !!
        index = index + 1
        

#-------------------------------------------------------------------------------| ACCESS CHAPTER URL |
for item in html_request(URL).select(".row a"):   
    low = item
    low = str(low).lower()
    data_list.append(getdata_dict(low))
    chapter_urls.append(item.get('href'))
    
#---------------------------------------------------------------------------------| ACCESS IMAGE URL |
for item_a in chapter_urls:
    image_list = []
    for item_b in html_request(item_a).select("#vungdoc img"):
        image_list.append(item_b.get('src'))
    data_list[index].update( {'img': image_list})
    index = index + 1

#-----------------------------------------------------------------------------------------| DOWNLOAD |
dwnld(data_list)