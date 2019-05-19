#-----------------------------------------------------------------------------------------| IMPORTS |
import urllib.request 
from bs4 import BeautifulSoup 
import re
import os

#---------------------------------------------------------------------------------------| VARIABLES |
URL = 'https://manganelo.com/manga/tales_of_demons_and_gods'
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
    #for item in length ?!
    index = 0
    temp_t = data[index]['title']
    temp_p =  os.getcwd()
    path_p = 'C:\\ComicCrawler\\{}'
    
    try:
        if not os.path.exists(path_p.format(temp_t)):
            os.makedirs(path_p.format(temp_t)) 
    except OSError:
        print("Creation of the parent directory failed")

    os.chdir(path_p.format(temp_t))

    for item in data[index]['img']:
        temp_c = data[index]['chapter']
        temp_n = data[index]['chapter_name']
        path_c = temp_p + '{}' + '{}'

        try:
            if not os.path.exists(path_c.format('\\Chapter_' + temp_c, '-' + temp_n)):
                os.mkdir(path_c.format('\\Chapter_' + temp_c, '-' + temp_n)) 
            else:
                os.chdir(path_c.format('\\Chapter_' + temp_c, '-' + temp_n))
        except OSError:
            print("Creation of the chapter directory failed")

        #----------------------------------------------------------------------------| IMAGE REQUEST |
        filename = item.split('/')[-1] 
        urllib.request.urlretrieve(item, path_c) !! SERVER_ERROR 403 !!
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