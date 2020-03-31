# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 23:56:27 2020

@author: Terentak
"""

from bs4 import BeautifulSoup

import requests
import shutil
import string
    
def download_images(chapter_url):  
    
    c_result = requests.get(chapter_url)
    c_content = c_result.content
    c_soup = BeautifulSoup(c_content, features="lxml")
    
    div_tags = c_soup.find("div", "container-chapter-reader")
    img_tags = div_tags.find_all("img") 
    
    image_list = []
    
    for image_url in img_tags:
        image_list.append(image_url.get('src'))
        
    ss = 1
    for image in image_list:
        
        resp = requests.get(image, stream = True)
        local_file = open("image" + str(ss) + ".png", 'wb')
        resp.raw.decode_content = True
        shutil.copyfileobj(resp.raw, local_file)
        del resp
        ss+=1
        
        
        
def non_alpha(seq):
    new = ''
    for letter in seq:
        if not letter.isalpha():
            new += letter
    new = new.strip()
    return new
        

def slugify(s):
        """Take a string and return a valid filename constructed from the string.
        Uses a whitelist approach: any characters not present in valid_chars are
        removed. Also spaces are replaced with underscores(not).
         
        Note: this method may produce invalid filenames such as ``, `.` or `..`
        When I use this method I prepend a date string like '2009_01_15_19_46_32_'
        and append a file extension like '.txt', so I avoid the potential of using
        an invalid filename.
        """
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        filename = ''.join(c for c in s if c in valid_chars)
        #filename = filename.replace(' ','_') # I don't like spaces in filenames.#i dont mind
        return filename