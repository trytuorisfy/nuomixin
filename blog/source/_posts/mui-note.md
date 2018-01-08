title: MUI笔记
date: 2015-04-20 15:48:23
tags: 前端
---

[先上官网](http://dcloudio.github.io/mui/)
踩过的坑

坑1：
用HBuilder打包后，卡在图片界面进不去，结果发现，尼玛配置里面

        "plus": {
        "splashscreen": {
            "autoclose": true,/*是否自动关闭程序启动界面，true表示应用加载应用入口页面后自动关闭；false则需调plus.navigator.closeSplashscreen()关闭*   就是这里！！ 改成true！！！/
            "waiting": true/*是否在程序启动界面显示等待雪花，true表示显示，false表示不显示。*/
        },


坑2：
左边侧边栏往右滑时出现，但会影响页面中其他滑动，解决方法去掉mui-draggable
原来

    <div class="mui-off-canvas-wrap mui-draggable">
后来

    <div class="mui-off-canvas-wrap">  //哈哈 向右拖拽不会出侧边栏咯 yoyoyo


经验教训，那就是直接去[github](https://github.com/dcloudio/mui)看例子！！
