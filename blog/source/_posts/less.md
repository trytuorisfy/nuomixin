title: less
date: 2015-10-19 15:43:47
tags: 前端
---

笔记类
<!--more-->
之前用的一直是它的皮毛，决定再看下文档，把自己决定能用到的记录下。

定义变量
	
	//常用
	@nice-blue: #5B83AD;
	@light-blue: @nice-blue + #111;

	#header {
	  color: @light-blue;
	}

	//用于url
	// Variables
	@images: "../img";

	// Usage
	body {
	  color: #444;
	  background: url("@{images}/white-sand.png");
	}	

Mixins
	
	//input
	.my-mixin {
	  color: black;
	}
	.my-other-mixin() { //带括号，这个class本身就不输出了
	  background: white;
	}
	.class {
	  .my-mixin;
	  .my-other-mixin;
	}
	//output
	.my-mixin {
	  color: black;
	}
	.class {
	  color: black;
	  background: white;
	}

	//Namespaces
	#outer {
	  .inner {
	    color: red;
	  }
	}

	.c {
	  #outer > .inner;
	}	

适配相关
	
	//input
	.screen-color {
	  @media screen {
	    color: green;
	    @media (min-width: 768px) {
	      color: red;
	    }
	  }
	  @media tv {
	    color: black;
	  }
	}
	//output
	@media screen {
	  .screen-color {
	    color: green;
	  }
	}
	@media screen and (min-width: 768px) {
	  .screen-color {
	    color: red;
	  }
	}
	@media tv {
	  .screen-color {
	    color: black;
	  }
	}	

作用域
	
	//方式一
	@var: red;

	#page {
	  @var: white;
	  #header {
	    color: @var; // white
	  }
	}
	
	//方式二
	@var: red;

	#page {
	  #header {
	    color: @var; // white
	  }
	  @var: white;
	}

引入其他css

	@import "library"; // library.less
	@import "typo.css"	