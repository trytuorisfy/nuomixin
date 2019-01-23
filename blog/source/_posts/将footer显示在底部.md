---
title: 将footer显示在底部
date: 2018-01-02 15:21:22
tags: 亲测
---

需求说来也简单，就是让footer显示在底部，嗯，听着是挺简单的，结果那心酸也是不说了。直接上结果。
布局如下；
![现有布局](http://images.nuomixin.com/footerbuju.jpg?imageView2/2/w/400/q/75|imageslim)

解决方案：
设置内容区的最小高度。

内容区的最小高度 = 页面可见区域的高度 - 头部高度 - 尾部高度 - 20   //其中20就是为了别太挤了，预留了点空间，随意了。同时考虑到窗口缩放的影响，于是也监听了下窗口的resize

贴代码:
		
		setMinHeight();

	    $(window).resize(function() {
	        setMinHeight();
	    });

		function setMinHeight(){ //.content-wrapper指的是内容区 
	     	var minHeight = (document.documentElement.clientHeight - 120) + 'px'; //120 = 50 + 50 + 20(头部高度 + 尾部高度 + 留白高度)
	     	$('.content-wrapper').css('min-height',minHeight);
		}