import bs4, requests, re

WEB = 'https://news.yandex.ru/yandsearch?lr=213&cl4url=ria.ru%2Feconomy%2F20161205%2F1482815380.html&lang=ru&rubric=computers&from=index'
text = requests.get(WEB).text
soup = bs4.BeautifulSoup(text,'html.parser')
soup_res = soup.find('div', attrs={'class':'story__list'})
tags = soup_res.find_all('a', attrs={'class':'link link_theme_normal i-bem'})
webs_ls = []
for tag in tags:
    if tag['href'].startswith('http'):
        webs_ls.append(tag['href'])
word_sets = []
for elem in webs_ls:
    text = requests.get(elem).text
    soup = bs4.BeautifulSoup(text, 'html.parser')

    for elem in soup.find_all('p'):
        if len(elem.parent.parent.find_all('p'))>1:
            right_tags = elem.parent.parent.find_all('p')
            break
    new_words = []
    for elem in right_tags:
        wut=re.sub('[^а-яёa-z0-9]'," ", elem.text.lower()).split(' ')
        new_words+=(filter(None, wut))
    word_sets.append(set(new_words))
uniqueness = word_sets[0]
lulness = word_sets[0]
for setto in word_sets:
    uniqueness = uniqueness & setto
    lulness = lulness ^ setto
print(uniqueness)
print(lulness)
