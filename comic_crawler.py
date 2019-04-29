import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.request import Request



Url = "https://manganelo.com/manga/berserk_of_gluttony"


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
  chapter_tags = parsed_html.select(".row a") #select .row = selects row tags leerzeicen --> untertag a.

  for tag in chapter_tags:
    print(tag)


findChapterUrls(html)




