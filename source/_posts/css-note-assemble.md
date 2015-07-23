title: css笔记集合
date: 2014-12-03 17:49:02
tags: 前端
---
终于把电脑里扔了好久的js撸完了，把css也撸一下。
还是那句话，这些是到处收集来的笔记，非原创。
更新的会写上来源，以前库存的就抱歉了，因为不知道从哪收集来的了。

<!--more-->

# CSS 笔记撸起来
## 布局类
#### 分栏高度自动相等
	margin-bottom:-3000px; padding-bottom:3000px;
说明：核心CSS代码部分的3000像素是个可变值，如果您的分栏高度不可能高度超过2000像素，您就可以设为2000像素，如果会超过3000像素，那么您要修改值为4000像素或是更高。
	父标签的overflow:hidden属性是必须的，否则会显示溢出的内容。
CSS代码：
	#test{overflow:hidden; zoom:1;}
	.left{width:200px; margin-bottom:-3000px; padding-bottom:3000px; background:#cad5eb; float:left;}
	.right{width:400px; margin-bottom:-3000px; padding-bottom:3000px; background:#f0f3f9; float:right;}
	.center{height:300px; margin:0 410px 0 210px; background:#ffe6b8;}
HTML代码：

	<div id="test">
		<div class="left">左边，无高度属性，自适应于最高一栏的高度</div>
		<div class="right">右边，无高度属性，自适应于最高一栏的高度</div>
		<div class="center">中间，高度300像素，左右两栏的高度与之自适应</div>
	</div>
## 适配类
####屏幕宽度
	//Max Width
	@media screen and (max-width: 600px) {
	}
	//Min Width
	@media screen and (min-width: 900px) {
	}
	//Multiple Media Queries
	@media screen and (min-width: 600px) and (max-width: 900px) {
	}
	//Device Width
	@media screen and (max-device-width: 480px) {
	}　
#### css link时适配
	//设备像素比
	<link rel="stylesheet" media="only screen and (-webkit-min-device-pixel-ratio: 2)" type="text/css" href="iphone4.css" />
	//横屏和竖屏
	<link rel="stylesheet" media="all and (orientation:portrait)" href="portrait.css"> 
	<link rel="stylesheet" media="all and (orientation:landscape)" href="landscape.css">　
	//屏幕大小
	<link rel="stylesheet" media="screen and (max-width: 600px)" href="small.css" />
## 页面高宽相关
#### 原生js获取
	网页可见区域宽：document.body.clientWidth; 
	网页可见区域高：document.body.clientHeight; 
	网页可见区域高：document.body.offsetWidth   
	(包括边线的宽);
	网页可见区域高：document.body.offsetHeight 
	(包括边线的宽);
	网页正文全文宽：document.body.scrollWidth; 
	网页正文全文高：document.body.scrollHeight; 
	网页被卷去的高：document.body.scrollTop; 
	网页被卷去的左：document.body.scrollLeft; 
	网页正文部分上：window.screenTop; 
	网页正文部分左：window.screenLeft; 
	屏幕分辨率的高：window.screen.height; 
	屏幕分辨率的宽：window.screen.width; 
	屏幕可用工作区高度：window.screen.availHeight; 
	屏幕可用工作区宽度：window.screen.availWidth;
#### jquery获取
	获取浏览器显示区域（可视区域）的高度 ：   
	$(window).height();   
	获取浏览器显示区域（可视区域）的宽度 ：
	$(window).width();   
	获取页面的文档高度   
	$(document).height();   
	获取页面的文档宽度 ：
	$(document).width(); 
	浏览器当前窗口文档body的高度：  
	$(document.body).height();
	浏览器当前窗口文档body的宽度： 
	$(document.body).width();
	获取滚动条到顶部的垂直高度 (即网页被卷上去的高度)  
	$(document).scrollTop();   
	获取滚动条到左边的垂直宽度 ：
	$(document).scrollLeft(); 
	获取或设置元素的宽度：
	$(obj).width();
	获取或设置元素的高度：
	$(obj).height();
	某个元素的上边界到body最顶部的距离：obj.offset().top;（在元素的包含元素不含滚动条的情况下）
	某个元素的左边界到body最左边的距离：obj.offset().left;（在元素的包含元素不含滚动条的情况下）
	返回当前元素的上边界到它的包含元素的上边界的偏移量：obj.offset().top（在元素的包含元素含滚动条的情况下）
	返回当前元素的左边界到它的包含元素的左边界的偏移量：obj.offset().left（在元素的包含元素含滚动条的情况下）
## css3动画
先让我吐个槽 各种前缀 简直要瞎了 幸好我都是复制黏贴的
使用方法，给div加上这些class就好了，比如

    <div class='animated bounceoutleft'></div>
基础部分走起

	.animated{
		-webkit-animation-duration: 10s;//一轮动画所需时间
		-moz-animation-duration: 10s;
		-o-animation-duration: 10s;
		animation-duration: 10s;
		-webkit-animation-fill-mode: both;//动画时间之外的状态,'none'不改变默认行为;'forwards'动画完成后保持最后一个属性值（在最后一个关键帧中定义）;'backwards'在 animation-delay 所指定的一段时间内，在动画显示之前，应用开始属性值（在第一个关键帧中定义）;'both'向前和向后填充模式都被应用
		-moz-animation-fill-mode: both;
		-o-animation-fill-mode: both;
		animation-fill-mode: both;	
		animation-iteration-count:infinite;//播放次数 n（次数）|infinite（无限）
		-webkit-animation-iteration-count:infinite;			
	}
效果部分走起，这是个从中间移动到最左边渐隐的效果。要看效果→[戳我](http://tuorisfy.qiniudn.com/jianshu/html/cssnote-animate.html)

	.animated.bounceoutleft {
		-webkit-animation-name: bounceoutleft;//动画名字
		-moz-animation-name: bounceoutleft;
		-o-animation-name: bounceoutleft;
		animation-name: bounceoutleft;
	}	
	@-webkit-keyframes bounceoutleft {
		0% {
			left: 50%;
		}
		100% {
			left: 0;
			opacity: 0;
		}
	}
	@-moz-keyframes bounceoutleft {
		0% {
			left: 50%;
		}
		100% {
			left: 0;
			opacity: 0;
		}
	}
	@-o-keyframes bounceoutleft {
		0% {
			left: 50%;
		}
		100% {
			left: 0;
			opacity: 0;
		}
	}
	@keyframes bounceoutleft {
		0% {
			left: 50%;
		}
		100% {
			left: 0;
			opacity: 0;
		}
	}


一样在理，来个属性一览

	animation: name duration timing-function delay iteration-count direction;//组合写法
	animation-name: keyframename|none;
	animation-duration: time;
	animation-timing-function: linear|ease|ease-in|ease-out|ease-in-out|cubic-bezier(n,n,n,n);
	animation-delay: time;
	animation-iteration-count: n|infinite;
	animation-direction: normal|alternate;

## 网页字体设置
来源：[http://ued.ctrip.com/blog/?p=3589](http://ued.ctrip.com/blog/?p=3589)
 移动端项目：

    font-family:Tahoma,Arial,Roboto,"Droid Sans","Helvetica Neue","Droid Sans Fallback","Heiti SC",sans-serif;
pc端(含Mac)项目：

     font-family:Tahoma,Arial,"Helvetica Neue","Hiragino Sans GB",Simsun,sans-serif;
移动和pc端项目：

    font-family:Tahoma,Arial,Roboto,"Droid Sans","Helvetica Neue","Droid Sans Fallback","Heiti SC","Hiragino Sans GB",Simsun,sans-serif;

## 各种零散tips
#### 不显示文字
	text-indent: -9999em;
	overflow: hidden;
	float: left; //当然也可以float: right;
#### 超过显示范围后变点点
	display: inline-block;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
	width: 190px; //宽度一定要加
#### 子元素浮动，父元素要有高
	overflow:auto;zoom:1;//①让父元素自己浮动起来也有高，这办法可以临时用用 看看子元素整体占的大小;②子元素浮动父元素absolute可以去除浮动影响
### ie9以下通用hack
	color#0000FF\9;所有IE浏览器(IE6+)支持；
### ul中的li居中
	ul {
		text-align: center;
	}

	li {
		 display: inline;
		 float: none;
		 _float: left;//IE6
		 margin-right: 5px;//间隔
	}
#### 图片垂直居中
	.img{
		vertical-align:center;
	}
#### a链接去掉虚线
手机端的firefox会有这个问题
直接

    a{ outline:none; } 
#### image-set实现Retina屏幕下图片显示
    background-image: -webkit-image-set(url(images/pic_1x.png) 1x,url(images/pic_2x.png) 2x);
#### iphone6兼容
    @media (device-width:375px) and (-webkit-min-device-pixel-ratio:2){/* 兼容iphone 6 */
    .class{}
    }
    @media (device-width:414px) and (-webkit-min-device-pixel-ratio:2.6){/* 兼容iphone6 plus */
    .class{}
    }
#### 修改select样式
    .test_select{
        line-height: 32px;
        border-color: #fff;
        /*border: 1px solid #ccc;*/
        border-radius: 3px;
        padding: 3px;
        vertical-align: middle;
    }
    :-webkit-any(.test_select){
        height: 34px;
        line-height: 24px;
        background-position: right 3px;
        background-repeat: no-repeat;
        background-image: url(images/angle.fw.png);
    };
***
撸完，收工！



