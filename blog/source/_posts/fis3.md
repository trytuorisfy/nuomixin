title: fis3
date: 2015-10-16 10:05:26
tags: 笔记
---
边看边记录吧，岁数大了，记性不行了
<!-- more -->
配置文件：fis-config.js
## 发布
	
	//发布到本地
	fis3 release -d <path>//示例 fis3 release -d ../output(发布到上级目录的output文件夹)

	//发布到远程机器（修改配置文件）
	fis.match('*', {
	  deploy: fis.plugin('http-push', {
	    receiver: 'http://cq.01.p.p.baidu.com:8888/receiver.php',
	    to: '/home/work/htdocs' // 注意这个是指的是测试机器的路径，而非本地机器
	  })
	})	

## 配置文件

	// fis-config.js

	//配置文件发布位置
	fis.match('*.{png,js,css}', {
	  release: '/static/$0'
	});
	
	//增加md5戳
	fis.match('*.{js,css,png}', {
	  useHash: true
	});

	//资源压缩
	fis.match('*.js', {
	  // fis-optimizer-uglify-js 插件进行压缩，已内置
	  optimizer: fis.plugin('uglify-js')
	});

	fis.match('*.css', {
	  // fis-optimizer-clean-css 插件进行压缩，已内置
	  optimizer: fis.plugin('clean-css')
	});

	fis.match('*.png', {//题外话 妈妈再也不用担心我的压缩图片问题了
	  // fis-optimizer-png-compressor 插件进行压缩，已内置
	  optimizer: fis.plugin('png-compressor')
	});	

	//CssSprite图片合并(仅对CSS 中路径带 ?__sprite图片并且分配到 useSprite: true 的 CSS 文件才会被处理)
	// 启用 fis-spriter-csssprites 插件
	fis.match('::package', {
	  spriter: fis.plugin('csssprites')
	})

	// 对 CSS 进行图片合并
	fis.match('*.css', {
	  // 给匹配到的文件分配属性 `useSprite`
	  useSprite: true
	})	

	//如果开发环境不需要如上功能，再加上下面这段
	fis.media('debug').match('*.{js,css,png}', {
	  useHash: false,
	  useSprite: false,
	  optimizer: null
	})

## 调试

	//启动服务
	fis3 server start // http://127.0.0.1:8080(默认)   //惊喜，竟然还生成了一个外网可以访问的地址，太棒了！
	
	//发布
	fis3 release //不加 -d 参数默认被发布到内置 Web Server的根目录下，当启动服务时访问此目录下的资源。

	//文件监听
	fis3 release -w

	//浏览器自动刷新
	fis3 release -wL	

	//打开内置web server目录
	fis3 server open

	//更多参数 
	fis3 server -h //start stop restart info open clean install(name)

## [嵌入资源](http://fis.baidu.com/fis3/docs/user-dev/inline.html)

## 插件
	
	//less预处理
	npm install -g fis-parser-less //安装插件（html直接引入.less文件）
	//配置文件
	fis.match('*.less', {
	  // fis-parser-less 插件进行解析
	  parser: fis.plugin('less'),
	  // .less 文件后缀构建后被改成 .css 文件
	  rExt: '.css'
	})

[简单打包](http://fis.baidu.com/fis3/docs/lv1.html)，有基于整个项目和基于页面的，我觉得基于页面的挺实用的，简单粗暴O(∩_∩)O

	//简单打包
	//插件装起来
	npm install -g fis3-postpackager-loader
	//配置文件一：整个项目都打在一起，成为一个css和一个js
	fis.match('::package', {
	  postpackager: fis.plugin('loader')
	});
	fis.match('*.{less,css}', {
	  packTo: '/static/aio.css'
	});
	fis.match('*.js', {
	  packTo: '/static/aio.js'
	});
	//配置文件二：基于页面的打包
	fis.match('::package', {
	  postpackager: fis.plugin('loader', {
	    allInOne: true
	  })
	});

## 零散知识
[时间戳](https://segmentfault.com/q/1010000003860300)
	
	//fis-conf.js
	fis.set('date', new Date);
	fis.match('*.{js,css,png,jpg}', {
	    query: '?t=' + (fis.get('date').getYear() + 1900) 
	                 + (fis.get('date').getMonth() + 1) 
	                 + (fis.get('date').getDate())
	                 + (fis.get('date').getHours())
	                 + (fis.get('date').getMinutes())
	});
[相对地址插件](https://github.com/fex-team/fis3-hook-relative)

	//fis-conf.js
	// 启用插件
	fis.hook('relative');

	// 让所有文件，都使用相对路径。
	fis.match('**', {
	  relative: true
	})

### 增加md5戳
在网上搜了一遍，没啥办法，突然发现个地方说其实可以改源码，[我的灵感来源](http://www.longlong.asia/2015/09/20/fis3-static-control.html)
直接贴测试成功的修改方式，就改2个地方就可以了
修改fis3里面的lib/file.js文件
	
	//fis3中的lib/file.js
	//修改一 在60行左右
	function addHash(path, file) {
	  var rExt = file.rExt,
	    qRExt = fis.util.escapeReg(rExt),
	    qExt = fis.util.escapeReg(file.ext),
	    hash = file.getHash(),
	    onnector = fis.media().get('project.md5Connector', '_'),
	    reg = new RegExp(qRExt + '$|' + qExt + '$', 'i');
	  // return path.replace(reg, '') + onnector + hash + rExt;//原始版
	  return path;//md5版，文件名保持不变
	}
	//修改二 在480行左右
	getUrl: function() {
	    var url = this.url;
	    if (this.useHash) {
	      // url = addHash(url, this); //原始版
	      url += '?' + this.getHash(); //md5版
    }

    //项目中的配置文件 fis-conf.js
    //md5戳可用 了
	fis.match('*.{js,css,png,jpg}', {
	  useHash: true
	});

最后叨逼一句，度受的源代码的注释写的太棒了，让我个渣渣也找到地方改了