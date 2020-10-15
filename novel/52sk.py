# coding=utf-8

import time
import requests
from lxml import etree

from urllib.parse import urlparse
 


count = 0
txtName = ''
tryTime = 0
urlPre = ''

def next_page(url):
    print('next_page')
    try:
        get_page(url)
    except:
        print('next except')
        print(url)
        # browser.refresh()
        # return next_page(page_num)
        # return 
        get_page(url)


def get_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
        }
        html = requests.get(url, headers=headers)
        html.encoding = html.apparent_encoding
        text = etree.HTML(html.text)
        save_to_txt(text,url)
    except:
        global tryTime
        tryTime += 1

        print('get except')
        print(url)
        # browser.refresh()
        # return next_page(page_num)
        # return
        
        if tryTime < 4:
            next_page(url)
        else:
            return



def save_to_txt(text,url):
    global count
    global txtName
    if count == 0:
        # txtName = text.xpath('//h1/a/text()')[0] + '.txt'
        txtName = text.xpath('//h1/text()')[0] + '.txt'
        count += 1


    title = text.xpath('//*[@class="article-title"]/text()')[0]
    if title:
        print(title)
        # with open(txtName, 'a+', encoding='utf-8', errors='ignore') as f:
        #     f.write(title)  # 文件的写操作
        content = text.xpath('//*[@class="article-content"]/p/text()')
        # print('content')
        # print(content)
        for i in content:
            # str = i + '\n'
            with open(txtName, 'a+', encoding='utf-8', errors='ignore') as f:
                # f.write(str)  # 文件的写操作
                f.write(i + '\n')  # 文件的写操作

        next_url = urlPre + text.xpath('//*[@class="pagination2"]/ul[1]/a[3]/@href')[0]
        # print(next_url)


        get_page(next_url)
    else:
        print('没有title')



def main():
    try:
        url = 'https://www.52shuku.vip/yanqing/hy6m_2.html'
        global urlPre
        urlParms = urlparse(url)
        urlPre = ''
        # urlPre = urlParms.scheme + '://' + urlParms.netloc;
        # print(urlPre)
        get_page(url)
    finally:
        print('close')


if __name__ == '__main__':

    main()
    print('结束')
