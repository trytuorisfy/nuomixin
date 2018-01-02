title: fis + handlerbars 绝配！
date: 2015-01-21 16:03:55
tags: 前端
---
handlebars可以解决数据问题，让html好看多了，但公共部分的怎么搞定呢？难道再弄个模板啥的吗，本来想用shtml，但不一定服务器都支持啊。
突然 我想到了 可以用fis！！ 哈哈哈 就用原版的 就行咯~~
OMG 好久前看的 发现果然不用就是不记得的啊啊啊
算了 直接记录下来好了 
囧 我竟然发现 我已经写过一篇fis使用的笔记了 ....
那就直接撸起来
东西见 酷盘  fishandler
过程简介
安装fis及simple插件,less插件也安上

    npm install -g fis
    npm install -g fis-postpackager-simple
    npm install -g fis-parser-less


<!--more-->

**更新：不要用less插件 否则package后 仍然会有零散的css，那是less生成的！**
修改配置文件

    //Step 1. 取消下面的注释开启simple插件，注意需要先进行插件安装 npm install -g fis-postpackager-simple
	fis.config.set('modules.postpackager', 'simple');
	fis.config.set('modules.parser.less', 'less');
	fis.config.set('roadmap.ext.less','css');

	//通过pack设置干预自动合并结果，将公用资源合并成一个文件，更加利于页面间的共用

	//Step 2. 取消下面的注释开启pack人工干预
	fis.config.set('pack', {
	    'all.js': [
	        '/js/**.js'
	    ]
	});
	fis.config.merge({ //发布时命令为 fis release -D
	    roadmap : {
	        domain : "."
	    }
	});

开启服务器

    fis server start //开启服务器

在编辑的时候 要实时更新的话  releas这么写 修改后会自动刷新的

    fis release -wL

###重点来了 发布！

    fis release -pD -d ./output   //开启package，domain，输出到指定目录

我是掉坑里的补充说明
**要合并的文件要放在html中，比如index.html，不要放在被插入的模板中，比如 header.html，不然没办法合并！！！！**就是 fis release -p 你看到的还是原来的那种











