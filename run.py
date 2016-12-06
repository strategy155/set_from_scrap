import bs4, requests, re
from newspaper import ArticleException
from newspaper import Article
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
from operator import itemgetter

WEB = 'https://news.yandex.ru/yandsearch?lr=213&cl4url=ria.ru%2Feconomy%2F20161205%2F1482815380.html&content=alldocs&from=story'
text = requests.get(WEB).text
soup = bs4.BeautifulSoup(text,'html.parser')
soup_res = soup.find('div', attrs={'class':'story__main'})
tags = soup_res.find_all('a', attrs={'class':'link link_theme_normal i-bem'})
webs_ls = []
for tag in tags:
    if tag['href'].startswith('http'):
        webs_ls.append(tag['href'])
word_sets = []
webs_ls = set(webs_ls)
for elem in webs_ls:
    print(elem)
    extractor = Article(elem, language='ru')
    try:
        extractor.download()
        extractor.parse()
    except ArticleException:
        continue
    print(extractor.text)
    wut=re.sub('[^а-яёa-z0-9]'," ", extractor.text.lower()).split(' ')
    word_sets.append(list(filter(None, wut)))
uniqueness = set(word_sets[-1])
lulness = set(word_sets[-1])
wow = lulness
freq = {}
counter = 0
lulsum = 0
for elem1 in word_sets:
    counter+=1
    lulsum += len(set(elem1) & lulness)
thresh = lulsum/counter
for elem1 in word_sets:
    if len(set(elem1) & lulness) > thresh:
        wow = wow ^ set(elem1)
        uniqueness = uniqueness & set(elem1)
print(wow)
print(uniqueness)
# for setto in word_sets:
#     for elem in set(setto):
#         try:
#             freq[elem]+=1
#         except KeyError:
#             freq[elem] = 1
#     uniqueness = uniqueness & set(setto)
#     lulness = lulness ^ set(setto)
#
# truelulness = []
# for elem in lulness:
#     if freq[elem] > int(sum(freq.values())/len(freq)):
#         truelulness.append(elem)
#
# freq = OrderedDict(sorted(freq.items(), key = itemgetter(1) ))
# for elem in lulness:
#     print(elem,freq[elem])