---
title: 小说txt下载
date: 2018-01-05 17:24:56
tags: 亲测
---
windows环境下运行python下载小说保存成txt

本人不会写python，网上找的，加工了下，参见[python爬虫爬取某小说网站的小说 ](https://zwm-coder.github.io/2017/02/09/python%E7%88%AC%E8%99%AB%E7%88%AC%E5%8F%96%E6%9F%90%E5%B0%8F%E8%AF%B4%E7%BD%91%E7%AB%99%E7%9A%84%E5%B0%8F%E8%AF%B4/)

踩过的坑,缺python的插件。
解决方法，参见[【亲测好用！】Windows系统下安装Beautiful Soup4](https://seofangfa.com/shell/python-beautiful-soup.html)
总结下，就是先把插件下下来(列如	beautifulsoup4-4.3.2.tar.gz),解压缩(路径随意啦),再用cygwin进入解压缩后的目录,运行下 setup.py build 和 setup.py install

简单粗暴贴代码

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
	        print u"没有下一页啦".encode("GBK")
	        txtName = soup.select('h1')[0].get_text() + '.txt'
	        if os.path.exists(txtName):
	            os.remove(txtName)
	        f.close()
	        #重命名
	        os.rename('down.txt',txtName)
	getStory(Url)

淮上大大，万一看见了也请装作看不见，我是真爱粉... 一路追过来的，所以章节全买了呢orz 求轻拍...

给自己看的备忘录。
我这记性，看到这波代码后一脸懵逼，愣是想不起来python怎么跑起来的，以防万一，我还是给自己写下吧。
新建个txt文件，改后缀名为.py，列如 down.py 
把代码复制进去，打开cmd 进入存放的文件夹 输入down.py 完事



