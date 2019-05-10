import re

def getdata (a):

    #matches = re.search('title=\"([\w\s:\-!;\d\.]+)Chapter ([\d\.\s\w]+)(?:\s?: ([\w\s!]+))?\"', a)
    matches = re.search('title=\"(.+)chapter ([\d\.\s\w]+)(?:\s?: (.+))?\">', a)
    title = matches.group(1)
    chapter = matches.group(2)
    chapter_name = matches.group(3)
    return {'title': title, 'chapter': chapter, 'chapter_name': chapter_name}




