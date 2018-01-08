title: CSS自适应相关汇总
date: 2014-12-03 11:57:03
tags: 前端
---
东西比较零散，所以直接理一理。
这些东西都是自己写的，如果有问题，请轻拍！
## 1. iphone VS ipad
吐槽先，之前做了一版，因为iphone和ipad要用同一个页面，所以我傻兮兮的给iphone和ipad分别做样式，光css的行数就已经不忍直视了。
后来！！ 要改样式！！！ 当时我的内心的小人就在呐喊，oh！ no！！！
后来想出了个非常赞的解决方法，哈哈哈。

思路就是确定iphone和ipad内容部分宽度的大小，之间形成等比例关系，然后只要弄好iphone的样式，ipad的样式只要修改**em**就可了。

上关键点
- 设置rem
- 
	  html{
		font-size: 100px;//此时em('body'的字体大小)也为100px;因为'html'是父元素，'body'是子元素
	  }
- 判断iphone还是ipad
- 
	  <!-- 判断iphone还是ipad开始  -->
	  <script>
		getType();
	    function getType(){  
	    	var body = document.querySelector('body');
	    	// alert(body);
            if(navigator.userAgent.indexOf("iPhone") != -1) {  
            	body.style.fontSize = "50px";
                 
            }  
            if(navigator.userAgent.indexOf("iPad") != -1){  
                   
            }  
        };  	
	  </script>
	  <!-- 判断iphone还是ipad结束 -->
- html部分限定内容宽度
- 
	  <!-- wrap 通用 目标大小 ipad:640*960px,iphone:320*480px -->
	  <div class="wrap"></div>	

## 2. 所有尺寸根据屏幕大小重新计算
思路：通过读取屏幕宽度后，计算rem的值。
备注：不适合精细活，因为在适应屏幕重新计算时，小的地方会有些偏差，比如理论上来说有个图片应该是垂直居中的，但经过重新计算后，就有可能有点歪了。
在安卓手机上用过这个办法，ok。(吐个槽，安卓的分辨率要不要这么多啊，所以就这么办了！)

      //css部分
      html{font-size:100px;}//设置为100px只是为了便于计算
***

      //js部分
      var wrap_w = document.documentElement.clientWidth;
      var html = document.querySelector('html');   
      caculate(wrap_w);

      //尺寸适应
      window.onresize  = function(){
        var new_wrap_w =  document.documentElement.clientWidth;
        if(new_wrap_w < wrap_w){
            wrap_w = new_wrap_w;
            caculate(wrap_w);
        }
        
      }
      function caculate(wrap_w){
        var wrap_w =  document.documentElement.clientWidth;
        if(wrap_w > 980){ //980是内容宽度，也就是'wrap'设置的宽度
            wrap_w = 980;
        }
        var fs = parseInt(wrap_w/9.8);
        html.style.fontSize = fs + 'px';
      } 
## 3. 宽度按照百分比，高度固定
我发现这种还是比较实用的，高度固定后，写起来方便多了。至少垂直方向不会有啥偏的了。
在iphone上用过这个办法，ok。
就是类似这种css

    .test{width:20%;height:50px;}
***
收工！





