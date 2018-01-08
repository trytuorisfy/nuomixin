title: ajax跨域
date: 2015-05-06 15:04:42
tags: 前端
---
总有需要跨域的时候啊...好心酸的感觉哪...

	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>ajax跨域测试</title>
	</head>
	<body>
	<p>body</p>
	<script src="jquery-1.10.2.min.js"></script>
	<script>
		$(function(){
		    var ser_url = 'http://image.baidu.com/i?tn=baiduimagejson&word=girl&rn=2&pn=1'; //百度受受 小小用下你的api哈
		    $.ajax({
		        type : "GET",
		        url: ser_url,
		        dataType : "jsonp",
		        cache:false,
		        jsonp: "callback",//传递给请求处理程序或页面的，用以获得jsonp回调函数名的参数名(默认为:callback)
		        jsonpCallback:"jsonpcallback",//自定义的jsonp回调函数名称，默认为jQuery自动生成的随机函数名
		        success : function(data){
		        	console.log('sucess' + data)
		        	console.log(data.data[0].thumbURL)
		        }
			})

			function jsonpcallback(data){ 
				// console.log(data)  //函数内容用不到，但是需要存在这个函数      
	    	} 
	    });   	
	</script>	
	</body>
	</html>

