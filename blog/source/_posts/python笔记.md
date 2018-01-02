title: python笔记
date: 2016-08-03 09:58:29
tags: 后端
---

起服务
    
    //命令
    python -m SimpleHTTPServer 80  //后面的80端口是可选的，不填会采用缺省端口8000
    //访问地址
    http://localhost:80

<!--more-->

# Ubuntu环境下走起（虚拟机）
查看ip情况

    ifconfig //找到inet 地址的值，即需要的ip值，例如 192.168.11.111
    //app.py
    if __name__ == '__main__':
        app.run(host="0.0.0.0",port=5000,debug=True) //设置host即端口号

见证奇迹的时刻到了，直接在本机中(非虚拟机)访问192.168.11.111:5000就访问到接口啦，强势撒花



# 一些网站收集
[知乎](https://www.zhihu.com/question/29372574)




