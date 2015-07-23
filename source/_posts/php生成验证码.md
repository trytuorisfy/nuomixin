title: php生成验证码
date: 2015-02-06 10:46:47
tags: 后端
---


直接上网址 亲测好使！
[http://blog.csdn.net/leijiankun111/article/details/7256587](http://blog.csdn.net/leijiankun111/article/details/7256587)
作为个懒人 我要全部黏贴一下 哈哈哈 以后就不用找咯
<!--more-->

### testcode.php
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<title>验证码 走起</title>
		<style>
			.wrong{ color:red;}
			.right{ color:black;}
		</style>
		<script src="../js/jquery-1.10.2.min.js"></script>
		<script>
			function check_code(){
				var URL = "checkCode.php";
				var RequestData = 'action=checkcode&code='+$('#R-code').val();
				$.ajax({
					type:'POST',
					url:URL,
					data:RequestData,
					async:false,
					cache: false,
					success:function(responseData){
						var Result = eval('('+responseData+')');
						if(Result.verifycode=='Y'){
							$('#info-code').removeClass().html('验证码输入正确').addClass("right");
						}else {
							$('#info-code').removeClass().html('验证码输入错误').addClass("wrong");
						}
					}
				});
			}
			function refresh_code(){
				document.getElementById("imgcode").src="createCode.php?a="+Math.random();
			}
		</script>
	</head>
	<body>
	<?php 
	function getCodeHtml(){
		$codehtml='<div id="codetest">'
		         .'<h2>Code Test</h2>'
	             .'<label for="R-code">Code：</label>'
			     .'<img id="imgcode" src="createCode.php" alt="验证码" /><a href="javascript:refresh_code()">看不清？换一张</a><br>'
			     .'<input id="R-code"><span id="info-code"></span><br>'
		         .'<input type="button" onclick="check_code();" value="Check">'
	             .'</div>';
		echo $codehtml;
		}
	echo getCodeHtml();
	 ?>	
	</body>
	</html>
### createCode.php 
    <?php //生成验证码
         session_start();
         $codeNum=4;      //验证码个数
         $codeWidth=80;   //验证码宽度
         $codeHeight=18;  //验证码高度
         $code=' ';
         for($i=0;$i<$codeNum;$i++){  //生成验证码
    		 switch(rand(0,2))
    		 {
    			 case 0:$code[$i]=chr(rand(48,57)); break;   //数字
    			 case 1:$code[$i]=chr(rand(65,90)); break;   //大写字母
                 case 2:$code[$i]=chr(rand(97,122));break;   //小写字母
    			 }
    		 }
         $_SESSION["VerifyCode"]=$code;
         $image=imagecreate($codeWidth,$codeHeight);
         imagecolorallocate($image,255,255,255);
    	 //生成干扰像素
         for($i=0;$i<80;$i++){
    		 $dis_color=imagecolorallocate($image,rand(0,255),rand(0,255),rand(0,255));
             imagesetpixel($image,rand(1,$codeWidth),rand(1,$codeHeight),$dis_color);
    		 }
    	 //打印字符到图像
         for($i=0;$i<$codeNum;$i++){
    		 $char_color=imagecolorallocate($image,rand(0,255),rand(0,255),rand(0,255));
             imagechar($image,60,($codeWidth/$codeNum)*$i,rand(0,5),$code[$i],$char_color);
    		 }
         header("Content-type:image/png");
         imagepng($image);      //输出图像到浏览器
         imagedestroy($image);  //释放资源
    ?>
### checkCode.php
    <?php   
         session_start();  
         @$postcode = $_POST['code'];  
         if((strtoupper($postcode)) == strtoupper(($_SESSION["VerifyCode"])))   
         echo '{"verifycode":"Y"}';  
         else echo '{"verifycode":"N"}';  
    ?>

