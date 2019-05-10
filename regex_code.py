import urllib.request
from bs4 import BeautifulSoup
import re


URL = "https://manganelo.com/manga/tales_of_demons_and_gods"

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

def getdata (a):

<<<<<<< HEAD
=======
    #matches = re.search('title=\"([\w\s:\-!;\d\.]+)Chapter ([\d\.\s\w]+)(?:\s?: ([\w\s!]+))?\"', a)
>>>>>>> ff1faf744bfeb6fa5053fc90aed73f65f1947b1e
    matches = re.search('title=\"(.+)chapter ([\d\.\s\w]+)(?:\s?: (.+))?\">', a)
    title = matches.group(1)
    chapter = matches.group(2).zfill(3)
    chapter_name = matches.group(3)
    return {'title': title, 'chapter': chapter, 'chapter_name': chapter_name}


# headers={'User-Agent':user_agent,}
# request = urllib.request.Request(URL,None,headers) #The assembled request
# response = urllib.request.urlopen(request)

# data = response.read()
# soup = BeautifulSoup(data, 'lxml')


# for link in soup.select(".row a"):
#   link = str(link).lower()
#   comic_data = getdata(link)
#   print(comic_data)






