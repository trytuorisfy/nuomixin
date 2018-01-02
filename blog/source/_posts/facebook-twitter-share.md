title: Facebook和twitter的分享
date: 2015-10-10 16:10:11
tags: 前端
---
弄分享真是一把辛酸的泪，不吐槽了，直接上重点
## facebook
先附上debug的[网址](https://developers.facebook.com/tools/debug/),同时附上让我发现这个debug工具的[网页](http://fundesigner.net/facebook-cache/)
- 简单的就这么整
	https://www.facebook.com/sharer.php?u=http://www.baidu.com
- 复杂的就是需要拿权限，授权登陆后可以为用户发帖的
	贴个我测试的完整版好了

		<!DOCTYPE html>
		<html lang="en">
		<head>
		  <meta charset="UTF-8">
		  <title>facebook sharetest</title>
		</head>
		<body>
		<button onclick="myFacebookLogin()">Login with Facebook</button>
		   <script>
		    window.fbAsyncInit = function() {
		      FB.init({
		        appId      : '744032985725397', //进入开发者页面，可以查看已有的app的id
		        xfbml      : false,
		        version    : 'v2.5'
		      }); 
		    };
		    
		    (function(d, s, id){
		       var js, fjs = d.getElementsByTagName(s)[0];
		       if (d.getElementById(id)) {return;}
		       js = d.createElement(s); js.id = id;
		       js.src = "//connect.facebook.net/en_US/sdk.js";
		       fjs.parentNode.insertBefore(js, fjs);
		     }(document, 'script', 'facebook-jssdk'));
		      function myFacebookLogin() {
		        FB.login(function(){         
		          var abc = '变量测试';
		          var des = '看，一群帅哥！'
		          FB.api('/me/feed', 'post', {
	              	"message": abc,
	                "description": des,
	              	"link":"http://www.baidu.com"		            
		          });
		        }, {scope: 'publish_actions'});       
		      }    
		  </script>
		  
		</body>
		</html>

## twitter
在网上找到了一个[教程](https://petermahoney.net/make-a-share-on-twitter-link-with-url-and-hashtags/)，救我于水火。
所以直接用他的示例了

	http://twitter.com/share?text=Here’s an awesome tip!&url=https://petermahoney.net/make-a-share-on-twitter-link-with-url-and-hashtags/&hashtags=peter,is,awesome



