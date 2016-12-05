import bs4, requests

WEB = 'https://news.yandex.ru/yandsearch?lr=213&cl4url=ria.ru%2Feconomy%2F20161205%2F1482815380.html&lang=ru&rubric=computers&from=index'
text = requests.get(WEB).text
soup = bs4.BeautifulSoup(text,'html.parser')
soup_res = soup.find('div', attrs={'class':'story__list'})
tags = soup_res.find_all('a', attrs={'class':'link link_theme_normal i-bem'})
webs_ls = []
for tag in tags:
    if tag['href'].startswith('http'):
        webs_ls.append(tag['href'])
text = requests.get(webs_ls[0]).text
soup = bs4.BeautifulSoup(text, 'html.parser')
for elem in soup.find_all('p'):
    print(elem.text)