import bs4
from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup
import requests
import re
from types import SimpleNamespace
import os
from pathlib import Path
import shutil

def getImageData(url):   #input url ---> output: class() getImageData.filename,volume,chapter...
  matches = re.search('vol(\d+)_chapter_(\d+)_(\w+)/(\d+)\.jpg', url)
  volume = matches.group(1).zfill(3)
  chapter = matches.group(2).zfill(3)
  chapterName = matches.group(3)
  imageNumber = matches.group(4).zfill(3)
  filename = "volume_" + volume + '-chapter_' + chapter + '-' + chapterName + '-' + imageNumber + '.jpg'
  return SimpleNamespace(
    filename=filename,
    volume=volume,
    chapter=chapter,
    imageNumber=imageNumber,
    chapterName=chapterName
  )

def findImageUrls(html): #input html ---> output alle imageUrls
  page_soup = soup(html, "html.parser")
  image_tags = page_soup.findAll("img")
  imageUrls = map(lambda tag: tag.get("src"), image_tags)
  return filter(lambda url: '/r1/' in url, imageUrls)

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

# makes folders and subfolders (volume, chapter) --> returns path output/volume/chapter
def createDirectory(volume, chapter):
  path = Path("output/volume_" + volume + "/chapter_" + chapter)
  if os.path.exists(path) and os.path.isdir(path):
    shutil.rmtree(path)
  path.mkdir(parents = True, exist_ok = True)
  return path

def getChapter(tag): # ---> output: class() getChapter.url, title, volume, chapter
  url = tag.get("href")
  title = tag.get("title")
  volume = ''
  chapter = ''

  if title:
    matches = re.search('Vagabond Vol\.(\d+) Chapter (\d+)', title)
    if matches:
      volume = matches.group(1).zfill(3)
      chapter = matches.group(2).zfill(3)

  return SimpleNamespace(
    url = url,
    title = title,
    volume = volume,
    chapter = chapter
  )

def getChapters(url): #----> Liste mit allen Chaptern
  html = fetchPage(url)
  pageSoup = soup(html, "html.parser")
  linkTags = pageSoup.findAll("a")
  chapters = []
  for tag in linkTags:
    chapters.append(getChapter(tag))
  return filter(lambda chapter: chapter.volume and chapter.url and '/chapter/' in chapter.url and 'vagabond' in chapter.url, chapters)


baseUrl = 'https://manganelo.com/manga/read_vagabond_manga'

chapters = getChapters(baseUrl)
for chapter in chapters:
  path = createDirectory(chapter.volume, chapter.chapter)
  html = fetchPage(chapter.url)
  imageUrls = findImageUrls(html)

  for url in imageUrls:
    data = getImageData(url)
    name = path / data.filename

    img = requests.get(url).content
    with open(name, 'wb') as handler:
      handler.write(img)

# html = fetchPage(my_url)
# imageUrls = findImageUrls(html)

# for url in imageUrls:
#   data = getImageData(url)
#   name = data.filename
#   img = requests.get(url).content
#   with open(name, 'wb') as handler:
#     handler.write(img)





