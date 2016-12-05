import bs4, requests, re, operator
from newspaper import ArticleException
from newspaper import Article
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

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
uniqueness = set(word_sets[0])
lulness = set(word_sets[0])
freq = {}
for setto in word_sets:
    for elem in set(setto):
        try:
            freq[elem]+=1
        except KeyError:
            freq[elem] = 1
    uniqueness = uniqueness & set(setto)
    lulness = lulness ^ set(setto)
truelulness = []
for elem in lulness:
    if freq[elem] > int(sum(freq.values())/len(freq)):
        truelulness.append(elem)

sorted_freq = sorted(freq.items(), key=operator.itemgetter(1))
x_pos = np.arange(len(freq))
plt.bar(freq.keys(), freq.values(), align='center')
plt.xlabel('Performance')
plt.title('How fast do you want to go today?')
plt.show()