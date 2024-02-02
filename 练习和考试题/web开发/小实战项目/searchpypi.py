#! python3
# Open several Google search results.

import requests, sys, webbrowser, bs4

print('Searching...') # display text while downloading the search result page
#res = requests.get('http://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res = requests.get('http://pypi.org/search/?q=' + 'wordcloud')
#命令行执行方式，获取执行脚本后的参数，爬取指定网址
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features='html.parser')
#解析爬取的结果
linkElems = soup.select('.package-snippet')
#选择器选择指定的元素，生成一个bs4.element.ResultSet的列表
numOpen = min(5, len(linkElems))
#取最小值，如果列表长度大于5则取5，即最多循环打开5次
for i in range(numOpen):
    urlToOpen = 'http://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
