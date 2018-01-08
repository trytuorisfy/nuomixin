---
title: 百度云BAE上搭建hexo
date: 2018-01-02 14:34:04
tags: 亲测
---

本来用的是svn，换成git重新搭了一遍，记录下过程。

线上如下：
1.进入[百度云](https://cloud.baidu.com/)的管理控制台
2.进入应用引擎BAE
3.添加部署
4.类型选择"lighttpd-static",工具选择"git"
5.抠唧唧的我选择了64MB内存
6."下一步"完事

本地如下
前置内容：已安装好hexo($ npm install -g hexo-cli)
1.从部署列表里找到刚新建，"点击复制"复制下地址
2.git clone 复制的地址
3.我是新建了一个blog的文件夹
4.进入blog文件夹,以下参考[链接](http://www.famouscat.cn/2015/11/21/%E5%9C%A8BAE%E4%B8%8A%E6%90%AD%E5%BB%BAhexo/)

		$hexo init
		$npm install
		$npm install hexo-deployer-git --save

5.配置 _config.yml文件,appid其实就是clone下来的文件夹名,如appidv41db5n111
	deploy:
	  type: git
	  repo: https://git.duapp.com/[yourappid]
	  branch: master

6.$ hexo generate --deploy

注意：其实是只同步了public文件夹里面的内容。怪不得我还奇怪呢，怎么直接访问就对了呢，也不用改路径啊。
