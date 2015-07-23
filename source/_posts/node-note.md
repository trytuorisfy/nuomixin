title: node.js 好的教程
date: 2015-01-14 11:46:11
tags: 前端
---
[大赞的入门教程 express版本3.4.4](http://www.unfish.net/archives/772-20131207.html)
[上面版本的原版 express版本更新到4.x](http://cwbuecheler.com/web/tutorials/2013/node-express-mongo/)
[ghost博客教程](http://capbone.com/ghost/)
[一个在线平台的实例](http://www.cnblogs.com/gaojun/p/4153965.html)
以上亲测都有用
<!--more-->
注意点：
3.x版本 运行时 node xx.js
4.x版本 运行时  npm start
数据库连接上后 再执行 否则报错
[工具](http://xuyuan923.github.io/2014/09/25/nodejs-notes/) 其中提到的数据库软件[这里](http://yhv5.com/mongovue_480.html)
[robomongo](http://qianduanblog.com/post/nodejs-learning-12-robomongo-mongodb-client.html)
步骤简介，详细看教程

    install -g express
    npm install -g express-generator
    express nodetest1
package.json添加依赖

    "dependencies": {
        "express": "~4.0.0",
        "serve-favicon": "~2.1.3",
        "morgan": "~1.0.0",
        "cookie-parser": "~1.0.1",
        "body-parser": "~1.0.0",
        "debug": "~0.7.4",
        "jade": "~1.3.0",
        "mongodb": "*",
        "monk": "*"
    }
安装依赖

    npm install
新建data文件夹，用于存放数据库文件
重点来了！！express3.x版本 则是 node app
express4.x版本 npm start
吐个槽 怪不得之前用4的就没有成功启动过 坑爹啊！

    npm start
现在打开http://localhost:3000  应该是对了
后面的不写了 再写个重点 就是mongodb数据库
从官网下下来后 随便放哪里 再bin文件夹中建立个“连接到xx.cmd”名字任意，自己知道就好了 cmd内容如下

    mongod --dbpath "e:\wang\wang\nodejs\web\nodetest2\data"
过程简介如下：
先把“连接到xx.cmd”启动好，否则会报错！！（计算机积极拒绝）
命令行 进入到 mongodb的bin文件夹，输入“mongo”命令后出现version信息，connecting to：test

    mongo
    use nodetest2 //其实就是目标文件夹名
后面的再看教程

openshift上的mongodb数据
MongoDB 2.4 database added.  Please make note of these credentials:

   Root User:     admin
   Root Password: mAwD9Bk2N598
   Database Name: nodejs

Connection URL: mongodb://$OPENSHIFT_MONGODB_DB_HOST:$OPENSHIFT_MONGODB_DB_PORT/


***
##百度BAE搭建ghost注意点
提交代码报错时 提示 POST git-receive-pack (chunked)  

    git config http.postBuffer 524288000
放在BAE上的教程,重点看修改的地方
[ghost 0.4.2放到BAE上](http://www.ghostchina.com/install-ghost-in-bae-base-instalation/)
要用七牛云的话，有一个直接写好的0.4.2版本
[0.4.2带七牛云了](https://github.com/ghostchina/Ghost-0.4.2-qiniu)
***
又到了吐槽时间 本来想升级成0.5版本的 结果搞了半天老报错 后来 才发现  据说  百度受受上的node版本低了 所以不支持  OMG!!
最后还是安安心心用0.4版本吧 ai...
bae增加多说[增加多说](http://www.thebeet.cn/gei-ghostzeng-jia-duo-shuo-ping-lun-zu-jian/)
[好看的theme](https://marcosn.com/willsong-ghost-theme/)
[根据上面的这个自己改的主题](http://nuomixin.qiniudn.com/blog-willsong_wang.zip)
***
[科普框架](http://idlelife.org/archives/516)
[一个博客的详细教程](https://github.com/nswbmw/N-blog)




