title: 各种tips
date: 2015-07-22 11:12:57
tags: tips
---

各种零零散散的小内容，反正啥都有，都扔里面了咯~
## git
让windows Git设置为大小写敏感的命令如下

	git config core.ignorecase false 

提交时文件大小受到限制

	git config http.postBuffer 524288000

github添加ssh

- "Git Bash" 
- 键入命令：
	ssh-keygen -t rsa -C "email@email.com"
- 用记事本打开id_rsa.pub文件，复制内容，到github网站上到ssh密钥管理页面，添加新公钥，随便取个名字，黏贴内容

需要注意产生的密钥文件在当前用户的根目录，必须把这两个文件放到当前用户目录的“.ssh”目录下才能生效。如C:\Users\xxx\.ssh
## 网址收集
### html,css
[易企秀](http://eqxiu.com/#/home)
可以制作易于分享的html5动画效果，类似分享到朋友圈啥的，桌面端和手机端都可以访问，地址固定，修改后重新发布就行了。
### js
- [youmightnotneedjquery](http://youmightnotneedjquery.com/) 
	jquery对应的原生js写法

- [阮一峰的js教程](http://javascript.ruanyifeng.com/)

### 图片处理
[智图](http://zhitu.tencent.com/) 
腾讯的 压缩图片








