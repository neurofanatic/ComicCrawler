import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.request import Request



Url = "https://manganelo.com/manga/read_berserk_manga_online"


def fetchPage(url):  #input url -----> ouput: page_html
  req = Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
  )
  #opening connection grabbing the page
  uClient = uReq(req)
  page_html = uClient.read()
  uClient.close()

  return page_html

html = fetchPage(Url)

def findChapterUrls(html):
  parsed_html  = soup(html, "html.parser")
  chapter_tags = parsed_html.find_all(class_="row")
  atag  = []

  # for rowtag in chapter_tags:
  #   rowtag.find("a")

  # print(atag)

findChapterUrls(html)




