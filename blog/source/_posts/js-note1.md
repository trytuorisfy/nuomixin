title: JS笔记1
date: 2014-12-03 16:57:32
tags: 前端
---
一直想整理下笔记，但老是拖着。
简书也发现了好久，在同事那里看了一眼，有种一眼看中的感觉。
今天突然想到，用Markdown格式的话，要么直接用来写笔记好了。
而且也终于整明白七牛云存储怎么上传文件了，外链走起！
备注：这些都是笔记，主要都是收集的，非原创。

<!--more-->

# JS 笔记撸起来
## Ajax
这东西用的多，有用的代码贴起来
### 比较常规的
    $.ajax({ 
        async: false, 
        type : "POST", 
        url : "wallpaper.json",
        success : function(data) {
            var list = data.data.list;
            var row = "";      
            $("#Gallery").empty();
            $.each(data.data.list, function(index, item){
                row += '内容'        
            }); 
            $(row).appendTo($("#Gallery"));             
        },   
    });  
### 可以跨域的
#### 第一种
	$.ajax({
		type : "GET",
		url:"http://xxx.com/xx?xx=xx&callback=getcallback",
		dataType : "jsonp",
		cache:false,
		jsonp: "callback",//传递给请求处理程序或页面的，用以获得jsonp回调函数名的参数名(默认为:callback)
		jsonpCallback:"getcallback",//自定义的jsonp回调函数名称，默认为jQuery自动生成的随机函数名
		success : function(data){							
		}
	});
	function getcallback(data){	//留空	
	}	
#### 第二种
	window.url_prefix = "http://xxx.com/index.php?r=";

		$.getJSON( window.url_prefix + 'xxxx&jsoncallback=?', {}, function(data){
			alert(data.error);
	})
##各种零散
### jquery插件封装
    // 方法一
    (function($) {
        $.extend($.fn, {
            myplugin: function() {
                // your plugin logic
            }
        });
    })(jQuery);

    // 方法二
    (function($) {
        $.extend($.fn, {
            myplugin: function() {
                // your plugin logic
            }
        });
    })(jQuery);
### 数组排序
	kdata.sort( function(a, b){
		return parseInt(a["value" ]) < parseInt(b["value" ]) ? 1 : parseInt(a[ "value"]) == parseInt(b[ "value" ]) ? 0 : -1;
	}); 
### 闭包
    <script>
        function create(){
            var arr = new Array();  
         
            for (var i=0; i<10; i++){
                arr[i] = function(num){
                    return function(){
                        return num; 
                    };
                }(i);   
            }
         
            return arr;
        }
         
        var c_arr = create();
         
        for(var i=0; i<c_arr.length;i++){
            document.write("c_arr["+i+"] = "+c_arr[i]()+"<br />");    
        }    
    </script>
### 浏览器语言判断
	var type=navigator.appName;
	if (type=="Netscape"){
	    var lang = navigator.language;
	}
	else{
	    var lang = navigator.userLanguage;
	}
	var lang = lang.substr(0,2);
	if (lang == "zh"){

	}else{	

	}	
### 判断iphone ipad
    var lang=navigator.userLanguage||navigator.language; //这个可以用来读浏览器的语言
	var $C=location.hash;
	if (navigator.platform.indexOf('iPhone') != - 1 && $C!="#pc"){
	window.location.href="/en/v2/";
	}
	if (navigator.platform.indexOf('iPad') != - 1 && $C!="#pc"){
	    window.location.href="/en/v2/ipad.shtml";
	}
### 判断图片是否加载完成
	function loadImage(url, callback) {
	    var img = new Image(); //创建一个Image对象，实现图片的预下载
	    img.src = url;
	     
	    if(img.complete) { // 如果图片已经存在于浏览器缓存，直接调用回调函数
	        callback.call(img);
	        return; // 直接返回，不用再处理onload事件
	    }
	    img.onload = function () { //图片下载完毕时异步调用callback函数。
	        callback.call(img);//将回调函数的this替换为Image对象
	    };
	};
### 切割url
	var now_url=location.href; 获取当前url
	var parmpart= now_url.split("?")[1]; 以问号分割（会分成前后2部分）
	// var genreid = parmpart.split('&')[1].substring(8); 以&分割并且要第二个部分的第9个字符开始的内容（第几个用的时候再试试）
	var needid = parmpart.split('&')[0].substring(6);
谢谢  [@江枫](/users/848b56cd783a) 在评论中给出的取得url中参数值的方法，如下

	function getParameterByName(name) {
		name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
		var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
		results = regex.exec(location.search);
		return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
	}	
### 获取鼠标当前位置
	$(document).ready(function() {
		$().mousemove(function(e){
		$('# MouseCoordinates ').html("X Axis Position = " + e.pageX + " and Y Axis Position = " + e.pageY);
	});
### 回到顶部
	$(document).ready(function() {
		//when the id="top" link is clicked
		$('#top').click(function() {
			//scoll the page back to the top
			$(document).scrollTo(0,500);
		}
	});

### 所有链接都在新窗口打开
	$(document).ready(function() {
		//select all anchor tags that have http in the href
		//and apply the target=_blank
		$("a[href^='http']").attr('target','_blank');
	});
### 图片未加载完成则显示loading图片
[第一种 未封装](http://tuorisfy.qiniudn.com/jianshu/html/图片未加载完成则显示loading图片.html)
[第二种 封装](http://tuorisfy.qiniudn.com/jianshu/html/图片未加载完成则显示loading图片-封装版.html)




