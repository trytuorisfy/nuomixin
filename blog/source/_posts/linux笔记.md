title: linux笔记
date: 2016-06-23 15:43:28
tags: 笔记
---

决定入坑，做一个会用点linux的怪阿姨 orz
[教程](https://wizardforcel.gitbooks.io/w3school-linux/content/)来一发

#用到的命令
    
    //安装依赖，好简单粗暴啊
    sudo apt-get -f install
    //强制解锁
    sudo rm /var/cache/apt/archives/lock
    sudo rm /var/lib/dpkg/lock    

# 实用的命令

## [目录管理](https://wizardforcel.gitbooks.io/w3school-linux/content/8.html)

    ls: 列出目录
    cd：切换目录
    pwd：显示目前的目录
    mkdir：创建一个新的目录
    rmdir：删除一个空的目录
    cp: 复制文件或目录
    rm: 移除文件或目录

你可以使用 man [命令] 来查看各个命令的使用文档，如 ：man cp。

# mysql相关

    sudo netstat -tap | grep mysql //mysql是否在运行

    mysql -u root -p //进入
    show databases;
    use 数据库名;
    show tables;
[实用命令来一发](http://www.cnblogs.com/xdpxyxy/archive/2012/11/16/2773662.html)



# 黑魔法类
之前 my-sql-connector-python怎么都装不上，最后的解决办法

    sudo pip install --egg mysql-connector-python-rf

    sudo apt-get install python-jinja2 python-mysql.connector //这个不知道是不是一样的




