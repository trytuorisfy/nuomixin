#-*- coding:utf-8 -*-
import urllib2
import cookielib
from bs4 import BeautifulSoup
import codecs
import os
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#乐文小说
#第一章的地址
Url = "https://www.lewenxiaoshuo.com/books/yinhediguozhiren/5422053.html"
f = codecs.open("./down.txt",'w','utf-8')
def getStory(url):
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    result = opener.open(url)
    soup = BeautifulSoup(result,"html.parser")

    #获取小说内容
    content = soup.find_all(id="content")

    #获取章节标题
    bookName = soup.find_all(class_="bookname") and soup.select('h1')
    #将小说内容写入txt文本文档
    for i in content:
        new_str = i.get_text('<br>','\n')
        str = re.sub('<br>','\r\n',new_str)  #将文档中的<br>标签替换为换行符
        storyTitleCont = '第' + bookName[0].get_text().split(' ')[-1] + '章'
        storyTitle = "\r\n"+ storyTitleCont + "\r\n"
        print storyTitleCont
        f.write(storyTitle)
        f.write(str)
    #获取下一章的链接
    if soup.find_all(class_="bottem1"):
        nextUrls = soup.find_all(class_="bottem1")[0].find_all('a')
        next_url = nextUrls[2].attrs['href']
        #print next_url
        #函数递归
        getStory(next_url)
    else:
        print '没有下一页啦'
        txtName = soup.select('h1')[0].get_text() + '.txt'
        if os.path.exists(txtName):
            os.remove(txtName)
        f.close()
        #重命名
        os.rename('down.txt',txtName)
getStory(Url)