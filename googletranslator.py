#__author = "Tao Lin"
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from urllib2 import build_opener, Request, HTTPHandler, HTTPSHandler
import sys
import re
reload(sys)
sys.setdefaultencoding('utf8')

#Simulating user interactive action, pretend to visit "Google Traslate" by Mozilla Firefox browser
def translation(text, sourcelanguage = "en", translationlanguage = "zh-CN"):
    url = "http://translate.google.com/translate_a/t?client=t&hl=en&sl=" + sourcelanguage + "&tl=" + translationlanguage \
        + "&ie=UTF-8&oe=UTF-8&multires=1&prev=conf&psl=en&ptl=en&otf=1&it=sel.2016&ssel=0&tsel=0&prev=enter&oc"\
        "=3&ssel=0&tsel=0&sc=1&text=" + text.replace(' ', '%20').replace('\n', '')
    opener = build_opener(HTTPHandler(debuglevel=False), HTTPSHandler(debuglevel=False))
    request = Request(url, headers={'User-Agent': 'Mozilla/4.0'})
    open_download_file = opener.open(request, timeout=4)
    opener.close()
    #response (type: list) is the processed data Google Translate responses
    response = re.findall(r'"(.*?)"', re.search(r'\[\[\[(.*?)]],,"' + sourcelanguage + r'"', open_download_file.read().decode('utf-8')).group(1))
    iterator = (i for i in range(0, len(response), 4))
    return reduce(lambda x, y: x + y, [response[iterator.next()] for i in range(len(response)/4)])


#translation() parameters: text to translate, source language, translation language (such as en, zh-CN, ja, ru, de, fr).
#for more supported languages please visit https://cloud.google.com/translate/v2/using_rest#language-params
text = "Hello world!"
print(translation(text, "en", "zh-CN"))