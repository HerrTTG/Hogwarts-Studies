from DrissionPage import SessionPage

def getHTMLtext(url):
    r=SessionPage()
    r.get(url)
    ls=[]
    for tr in r.ele('css:#content-box > div.rk-table-box > table > tbody').eles('tag:tr'):
        _tmp = []
        if tr.eles('tag:td')[0].ele('@class^ranking'):
            _tmp.append(tr.eles('tag:td')[0].ele('@class^ranking').text)
        if tr.eles('tag:td')[1].ele('@class:univname-container'):
            _tmp.append(tr.eles('tag:td')[1].ele('@class:univname-container').ele('tag:img').attr('alt'))
        _tmp.append(tr.eles('tag:td')[-2].text)
        _tmp.append(tr.eles('tag:td')[-1].text)
        ls.append(_tmp)
    return ls

if __name__ =='__main__':
    ls=getHTMLtext('https://www.shanghairanking.cn/rankings/bcur/2023')
    for item in range(len(ls)):
        print(f'排名：{ls[item][0]} 学校：{ls[item][1]} 总分：{ls[item][2]} 办学层次：{ls[item][3]}')

    print('\n\n数据来源：https://www.shanghairanking.cn/rankings/bcur/2023')


