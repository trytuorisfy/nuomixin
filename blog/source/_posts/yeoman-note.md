title: Yeoman笔记
date: 2015-03-25 16:24:34
tags: 笔记
---
[教程看这里:http://bellyang.com/blog/post-700.html](http://bellyang.com/blog/post-700.html)
注意：
1. 安装时如果报缺少一个libiconv-2.dll
解决方法就是[点这里](http://lzw.me/a/git-libiconv-2-dll.html)
>将 Git\bin\ 下的 libiconv-2.dll 复制到 \Git\libexec\git-core\ 下。当前的 msysgit\bin 目录下没有 libiconv-2.dll 文件，在msysgit\mingw\bin 目录有这个文件，将其复制到 msysgit\bin 下就没有这个问题了。


2. 打包时 出现一个grunt jpg反正就是图片相关的错误时，就重新安装下等他装完就好了
       npm install grunt-contrib-imagemin

放到BAE上试了下 可以 就是没有连接到数据库的  数据库的还是试过。
grunt打包后 上传的时候 注意下
1. package.json中的启动的位置改好
2. server里的index里面的环境改成production
3. 端口改成百度受受的18080
应该差不多了 就这些