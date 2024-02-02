#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'https://xkcd.com' # starting url
os.makedirs('D:\\Python\\练习和考试题\\web开发\\小实战项目\\'+'xkcd', exist_ok=True) # store comics in ./xkcd
while not url.endswith('#'):
    # Download the page.
    print('From page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic > img')
    #选择器寻找图片的元素 图片元素在<div id ='comic'>中的img的属性中
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        #图片的地址保存在src属性的值里
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd.
        imageFile = open(os.path.join('D:\\Python\\练习和考试题\\web开发\\小实战项目\\'+'xkcd', os.path.basename(comicUrl)), 'wb')
        #写二进制非常重要
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        print('File %s Save successed' %(os.path.join('D:\\Python\\练习和考试题\\web开发\\小实战项目\\'+'xkcd', os.path.basename(comicUrl))))
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('#middleContainer > ul:nth-child(2) > li:nth-child(2) > a')[0]
    #选择器识别a类rel属性中值为prev的元素
    url = 'https://xkcd.com' + prevLink.get('href')
    #如果herf为#表示最后一页了，循环停止

print('Done.')