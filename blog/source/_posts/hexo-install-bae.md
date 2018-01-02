title: 在BAE上安装hexo
date: 2015-07-16 10:29:43
tags: 亲测
---
就说些关键内容。(我的系统是win7。hexo的命令需要进入node.js的命令行里输入)
## hexo部分
### 安装及使用
	//安装hexo
	npm install -g hexo

	//进入目录初始化
	hexo init
	
	//运行，会显示在localhost:4000
	hexo server

	//新建文章
	hexo new post 文章标题

	//生成内容
	hexo generate
流程就是这样了，用的主题是：[yilia](https://github.com/litten/hexo-theme-yilia)
里面有详细的配置，自己搞定就行

<!--more-->

## BAE部分
新建啥的就不说了，我选的是 **lighttpd-static**，纯静态，够用就行
直接说下注意点,我把整个hexo的目录都上传上去了，不仅仅是public文件夹
### 配置文件
app.conf中的url部分改成如下，将public文件夹作为访问的文件夹，[方法来源](http://ju.outofmemory.cn/entry/91774)

	- url : (.*)
	  script : /public/$1
### 主题yilia注意部分
若需要使用多说，修改themes\yilia\_config.yml,duoshuo部分改成如下:

	duoshuo: true
	duoshuo: "nuomixin" //你自己在多说的short_name
也是上面的文件，menu部分的链接需要写上具体的html，否则会跳转错误(这是我试了20个版本才试出来的Orz，不会写正则的人伤不起啊)

	menu:
		主页: /
		所有文章: /archives/index.html
		声控: /tags/声控/index.html

### 其他注意点
1. 如果修改了配置文件，需要重新生成下，即运行下hexo generate
2. 不需要的主题直接删了。（我配置的时候即使写了新主题，出来的还是默认的，删了默认的就好了）
***
大概就这样了，封。

补充下看到的好的hexo教程:
[安装](http://junzhepan.github.io/2015/03/17/Hexo-your-blog/)
[优化](http://junzhepan.github.io/2015/03/17/Hexo-%E4%BC%98%E5%8C%96/)
[添加搜索](http://www.jerryfu.net/post/search-engine-for-hexo-with-swiftype.html) 主题不一样，不会弄，我这智商啊....
[添加百度统计](http://blog.justforfun.top/2015/02/06/hexo-%E6%B7%BB%E5%8A%A0%E7%99%BE%E5%BA%A6%E7%BB%9F%E8%AE%A1/)
简述下：
1.编辑文件 themes/yilia/_config.yml ,添加一行配置：

    baidu_tongji: true
2.新建 themes/yilia/layout/_partial/baidu_tongji.ejs 内容如下:

	<% if (theme.baidu_tongji) { %>
	<script type="text/javascript">
	#申请的百度统计代码
	</script>
	<% } %>
3.编辑themes/yilia/layout/_partial/head.ejs 在 </head> 前添加:

	<%- partial("baidu_tongji") %> //是head.ejs 不是header.ejs!!
4.重新生成 
 
	hexo-generate


	





