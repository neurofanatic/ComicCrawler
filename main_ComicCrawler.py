#region | IMPORTS
import urllib.request
from bs4 import BeautifulSoup
import re
import regex_code as x
#endregion

#region | VARIABLES


URL = 'https://manganelo.com/manga/tales_of_demons_and_gods'
ChapterUrl = []
#endregion

#region | FUNCTION 1 | Input(URL) -> Output(html)                       | auf Internetseite zugreifen und parsen

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

headers={'User-Agent':user_agent,}
request = urllib.request.Request(URL,None,headers) #The assembled request
response = urllib.request.urlopen(request)

data = response.read()
soup = BeautifulSoup(data, 'lxml')
#endregion

#// region | FUNCTION 2 | Durchsuchen(html) -> Output(ChapterURL-Liste)    | nach a-tags suchen; Filterfunktionen
ChapterUrl = []

for link in soup.select(".row a"):
  ChapterUrl.append(link.get('href'))
  link = str(link).lower()
  comic_data = x.getdata(link)


  # print(link.get('href'))

print (ChapterUrl[1])


# for item in soup.select(".row a"):
#     test = item.get('title')
#     print(test[2])

# ATAG = soup.select(".row a")
# print(ATAG)
## print(ATAG[1].get('title'))
# print(chapter_name)

#endregion

#region | FUNCTION 3 | Regex -> Ordnerstruktur                          | Benennung und Ordnung der Daten

# matches = re.search('title=\"([\w\s:\-!;\d\.]+)Chapter ([\d\.\s\w]+)(?:\s?: ([\w\s!]+))?\"', URL)
# comic_title = matches.group(1)
# chapter = matches.group(2)
# chapter_name = matches.group(3)

#       .
#endregion

#region | FUNCTION 4 | Zugriff(ChapterURL) -> DONE                      | Suche nach Bildern; Download der Bilder
#       .
#       .
#endregion
