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
        txtName = text.xpath('//h1/a/text()')[0] + '.txt'
        count += 1


    title = text.xpath('//*[@id="nr_title"]/text()')[0]
    if title:
        print(title)
        with open(txtName, 'a+', encoding='utf-8', errors='ignore') as f:
            f.write(title)  # 文件的写操作
        content = text.xpath('//*[@id="nr1"]/text()')
        for i in content:
            str = i + '\n'
            with open(txtName, 'a+', encoding='utf-8', errors='ignore') as f:
                f.write(str)  # 文件的写操作

        next_url = urlPre + text.xpath('//*[@id="pb_next"]/@href')[0]
        get_page(next_url)
    else:
        print('没有title')



def main():
    try:
        url = 'https://m.meiguixs.net/html/127/127376/55982782.shtml'
        global urlPre
        urlParms = urlparse(url)
        urlPre = urlParms.scheme + '://' + urlParms.netloc;
        print(urlPre)
        get_page(url)
    finally:
        print('close')


if __name__ == '__main__':

    main()
    print('结束')
