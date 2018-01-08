title: angular.js + node.js +mongodb教程
date: 2015-03-20 10:38:25
tags: 前端
---

看这里！！[http://weblogs.asp.net/dwahlin/dynamically-loading-controllers-and-views-with-angularjs-and-requirejs](http://weblogs.asp.net/dwahlin/dynamically-loading-controllers-and-views-with-angularjs-and-requirejs)

对应的github看这里[https://github.com/trytuorisfy/CustomerManager](https://github.com/trytuorisfy/CustomerManager)

重点看这里！
导入数据到mongodb的步骤
>Load MongoDB Sample Data Option 1:
Load data into MongoDB by performing the following steps:
    Execute 'mongod' to start the MongoDB daemon
    Navigate to the CustomerManager/server directory (the one that has initMongoData.js in it)
    Execute 'mongo' to start the MongoDB shell
    Enter the following in the mongo shell to load the data seed file:
        use customermanager
        load("initMongoData.js")

其实做法应该是 
- 先到mongodb的文件夹中的bin文件夹
- 新建个文件“链接customermanager.cmd”，双击，内容如下 连接到要放数据的地方
      mongod --dbpath "e:\wang\Angularjs\CustomerManager-master\CustomerManager\server"
- 到项目的server文件夹中，有个“initMongoDB.bat”，内容如下
      @ECHO off
      e:\wang\mongodb\bin\mongo.exe %CD%\initMongoData.js
      ECHO -
      ECHO Your data is loaded
      pause
- 见证奇迹的时刻到了，打开MongoVUE.exe（一个看mongodb数据的软件）,连接上localhost之后，里面有个数据库就叫custormanager了，页面也有数据显示咯~~~


对了，这个还支持异步加载controller哦~
    


