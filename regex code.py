import re

Url = "https://manganelo.com/manga/read_berserk_manga_online"
matches = re.search('title=\"([\w\s:\-!;\d\.]+)Chapter ([\d\.\s\w]+)(?:\s?: ([\w\s!]+))?\"', Url)
# matches = re.search(r"title=\"([\w\s:\-!;\d]+)Chapter ([\d\.]+)(?:\s?: ([\w\s!]+))?\"", Url)
# matches = re.search('vol(\d+)_chapter_(\d+)_(\w+)/(\d+)\.jpg', url)
# comic_title = matches.group(1)

print(matches)
# if matches.group(1) is not None:
#     comic_title = matches.group(1)


# chapter = matches.group(2)
# chapter_name = matches.group(3)

