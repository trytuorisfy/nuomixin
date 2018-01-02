title: 自用的css基础库
date: 2015-05-06 15:03:57
tags: 前端
---
个人自用的基础css库，主要修改自张鑫旭的[quickLayout.css](http://www.zhangxinxu.com/wordpress/2014/03/quicklayout-css-%E5%BF%AB%E9%80%9F%E6%9E%84%E5%BB%BA%E7%BB%93%E6%9E%84%E5%85%BC%E5%AE%B9%E7%9A%84web%E9%A1%B5%E9%9D%A2/)备份。
<!--more-->


	body{
		font:12px/1.5 'Lucida Grande', Verdana, Arial, Sans-Serif;
		overflow: auto;
	}
	input,textarea,select{
		font:12px/1.5 'Lucida Grande', Verdana, Arial, Sans-Serif;
	}
	body,h1,h2,h3,h4,h5,h6,p,ul,ol,form{
		margin:0;
	}
	ul,ol,li{
		padding-left:0; 
		list-style-type:none;
	}
	/*image with no-border*/
	img{border:0;}
	/*css重置部分结束*/

	/*公共样式部分开始*/
	/* display */
	.dn{display:none;}
	.di{display:inline;}
	.db{display:block;}
	.dib{display:inline-block;} 
	/* margin */
	.m0{margin:0;}
	.mt0{margin-top: 0 !important;}
	.mr0{margin-right: 0 !important;}
	.mb0{margin-bottom: 0 !important;}
	.ml0{margin-left: 0 !important;}
	/* padding */
	.p0{padding:0;}
	.pt0{padding-top: 0;}
	.pr0{padding-right: 0;}
	.pb0{padding-bottom: 0;}
	.pl0{padding-left: 0;}
	/*border*/
	.bt0{border-top: 0 !important;}
	.bb0{border-bottom: 0 !important;}
	.bl0{border-left: 0 !important;}
	.br0{border-right: 0 !important;}
	/* width percent */
	.pct50{
		width: 50%;
	}
	.pct100{
		width: 100%;
	}
	/* font-size */
	.f0{font-size:0;}
	.f12{font-size:12px;}
	.f14{font-size:14px;}
	.f16{font-size:16px;}
	.f18{font-size:18px;}
	.f20{font-size:20px;}
	.f24{font-size:24px;}
	/* font-family */
	.fa{font-family:Arial;}
	.fs{font-family: Simsun;}
	.fm{font-family:'Microsoft Yahei';}
	/* font-style */
	.fb{font-weight:bold;}
	.fi{font-style:italic;}
	/* text-align */
	.tac{text-align:center;}
	.tar{text-align:right;}
	.tal{text-align:left;}
	.taj{text-align:justify;}
	/* text-decoration */
	.tdu{text-decoration:underline;}
	.tdn,.tdn:hover{text-decoration:none;}
	/* vertical-align */
	.vm{vertical-align:middle;}
	.vtb{vertical-align:text-bottom;}
	.vb{vertical-align:bottom;}
	.vt{vertical-align:top;}
	.vn{vertical-align:-2px;}
	/* color */
	.c0{color: #000;}
	.cf{color: #fff;}
	/* background color */
	.bg0{background-color: #000;}
	.bgf{background-color: #fff;}

	/* float */
	.fl{float:left;}
	.fr{float:right;}
	/* clear */
	.cl{clear:both;}
	/* position */
	.rel{position:relative;}
	.abs{position:absolute;}
	/*position values*/
	.t0{top: 0;}
	.r0{right: 0;}
	.b0{bottom: 0;}
	.l0{left: 0;}
	/*z-index*/
	.zi1{z-index:1;}
	/* cursor */
	.cp{cursor:pointer;}
	/* overflow */
	.ovh{overflow:hidden;}
	.ova{overflow:auto;}
	/* zoom */
	.z{*zoom:1;}

	/*块状元素居中*/
	.auto{margin: 0 auto;}
	/* 清除浮 动*/
	.fix{*zoom:1;}
	.fix:after{display:table; content:''; clear:both;}
	/*单行文字溢出虚点表示*/
	.ell{text-overflow:ellipsis; white-space:nowrap; overflow:hidden;}
	/*多行文字溢出虚点表示 移动设备有效 -webkit-line-clamp: 3 行数为3行*/
	.mell{display: -webkit-box;text-overflow: ellipsis;overflow : hidden;text-overflow: ellipsis;-webkit-line-clamp: 3;-webkit-box-orient: vertical;}
	/*隐藏文字*/
	.ti999{
		text-indent: -999em;
		overflow: hidden;
	}
	/* 大小不定元素垂直居中 */
	.dib_vm{display:inline-block; width:0; height:100%; vertical-align:middle;}
	/*公共样式部分结束*/
	/*右边方向阅读习惯的类别*/
	.tfr{
		direction:rtl;unicode-bidi: bidi-override;
	}
	.shadow{
		width: 100%;
		height: 100%;
		position: fixed;
		top: 0;
		bottom: 0;
		left: 0;
		right: 0;
		background-color: #000;
		opacity: 0.6;
		filter: alpha(opacity=60);   
	}
	/*隐藏文字*/
	.hide-text{
		white-space: nowrap;
		text-indent: 100%;
		overflow: hidden;
	 }
	 /*可用于安卓适配屏幕*/
	 .suit{ 
		position: absolute;
		top: 0;
		bottom: 0;
		left: 0;
		right: 0;
		overflow: hidden;    
	 }
	 /*按钮通用样式*/
	 .u-btn{
		display: inline-block;
		-webkit-box-sizing: content-box;
		-moz-box-sizing: content-box;
		box-sizing: content-box;
		padding: 0 1em;
		letter-spacing: 1px;
		word-spacing: normal;
		text-align: center;
		vertical-align: middle;
		cursor: pointer;
		text-decoration: none;
		color: #fff;
		padding: 0.8em 1.6em;
		background: #DFDFDF;
		border: 0;
	 }
	 /*placeholder文字颜色改变*/
	 /*WebKit browsers Mozilla Firefox 4 to 18  Mozilla Firefox 19+ Internet Explorer 10+*/
	 /*

		::-webkit-input-placeholder { 
		color:    #34466e;
		}
		:-moz-placeholder { 
			color:    #34466e;
		}
		::-moz-placeholder {
			color:    #34466e;
		}
		:-ms-input-placeholder { 
			color:    #34466e;
		}
	*/
	/*半透明背景色*/
	/*ie情况下 子元素要增加relative*/
	/*
	.trans{
		background-color: #277eff;
		filter: alpha(opacity=34);
		background: rgba(39, 126, 255, 0.34);
	}
	*/




	//一些新增内容
	font-family: "Roboto", "Helvetica Neue", "Hiragino Sans GB", "LiHei Pro", Arial, serif; //英文字体特别好看
	font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif;//中文来这发

	//补充滚动条跳动
	//[来源](http://www.zhangxinxu.com/wordpress/2015/01/css-page-scrollbar-toggle-center-no-jumping/)
	html {
	  overflow-y: scroll;
	}

	:root {
	  overflow-y: auto;
	  overflow-x: hidden;
	}

	:root body {
	  position: absolute;
	}

	body {
	  width: 100vw;
	  overflow: hidden;
	}

