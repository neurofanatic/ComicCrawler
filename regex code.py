import re
Url = "https://manganelo.com/manga/read_berserk_manga_online"
matches = re.search('title=\"([\w\s:\-!;\d\.]+)Chapter ([\d\.\s\w]+)(?:\s?: ([\w\s!]+))?\"', Url)
comic_title = matches.group(1)
chapter = matches.group(2)
chapter_name = matches.group(3)