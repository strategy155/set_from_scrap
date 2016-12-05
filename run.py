import bs4, requests, re
from newspaper import ArticleException
from newspaper import Article

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
    wut=re.sub('[^а-яёa-z0-9]'," ", extractor.text.lower()).split(' ')
    word_sets.append(list(filter(None, wut)))
uniqueness = set(word_sets[0])
lulness = set(word_sets[0])
freq = {}
for setto in word_sets:
    print(setto)
    for elem in set(setto):
        freq[elem]+=1

    # uniqueness = uniqueness & set(setto)
    # print(uniqueness)
    # lulness = lulness ^ set(setto)
    # print(lulness)
