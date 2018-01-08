title: JS笔记2
date: 2014-12-03 17:48:43
tags: 前端
---
笔记零零散散的记在各地方，再来一发。
还是那句话，到处收集的，非原创。
<!--more-->

##链接跳转
#### 判断PC和iphone 并用根据浏览器语言跳转页面
	var lang=navigator.userLanguage||navigator.language;
	var $C=location.hash;
	if (navigator.platform.indexOf('iPhone') != - 1 && $C!="#pc"){
		mobile_browse_lang();
	}else{
		pc_browse_lang();
	}
	function pc_browse_lang(){
        var type=navigator.appName;
        if (type=="Netscape"){
            var lang = navigator.language;
        }
        else{
            var lang = navigator.userLanguage;
        }
        var lang = lang.substr(0,2);

        var lang_key = ['key1', 'key2', 'key3', 'key4', 'key5'];//浏览器语言代码，若浏览器语言为英语，则对应为'en';
        // var lang_type = $.inArray(lang, lang_key); jquery写法


		function indexOf(lang_key, lang) {
		  for (var i = 0; i < lang_key.length; i++) {
		    if (lang_key[i] === lang)
		      return i;
		  }
		  return -1;
		}

		var lang_type = indexOf(lang_key, lang);


        if(lang_type == -1){
        	window.location.href = 'xxx_key0.html';//若不在  lang_key 数组里面 则默认为 key0
        } else {
        	window.location.href = 'xxx_'+ lang +'.html';
        }

	}
## 响应式相关
#### 用js进行获取窗口宽度，进行对应处理

    //牛逼版
    if(window.matchMedia){
        var mq = window.matchMedia("(min-width: 500px)");   
        mq.addListener(WidthChange);   
        WidthChange(mq); 
    }   

    function WidthChange(mq){
                if(mq.matches){

                //此时window的宽度大于500px

            }else{

                //此时window的宽度小于500px

            }  
    }

    //正常版
    var resizeMethod = function(){
        if (document.body.clientWidth < 768) {
            console.log('mobile');
        }
    };

    //绑定事件处理函数到resize事件
    window.addEventListener("resize", resizeMethod, true);  
#### 安卓手机分辨率判断计算
（自己算的 用于pc端和手机端是同一个页面的情况 等比缩放  这个大家随便看看 因为我也已经看不懂了 啊啊啊 当时的页面找不到了 oh no）

    var body = document.querySelector('body');
    var w = screen.width;//屏幕宽度
    var h = screen.height;//屏幕高度
    var rat = window.devicePixelRatio;//设备像素比  
    var s_w; 
    var c_w = document.documentElement.clientWidth;//可见区域宽度
    var c_h = document.documentElement.clientHeight;//可见区域高度
    if(w == c_w){//认为是pc端
        rat = 1;
    }
    //取到宽度（即取到较小的一个边的宽度）
    if( w > h){//横屏
        s_w = h; 
    }else{
        s_w = w;
    }   
    caculate();         
    function caculate(){
        var wrap_w;
        if(c_w < c_h){
            wrap_w = c_w;
        }else{
            wrap_w = s_w/rat;
        }
        if(wrap_w > 960){
            wrap_w =960;
        }
        var fs = parseInt(wrap_w/9.6);
        body.style.fontSize = fs+'px';

    }

## 数组相关
#### 查找数组符合项
    //jQuery
    $.inArray(item, array);                   
    //ie8+
    function indexOf(array, item) {
      for (var i = 0; i < array.length; i++) {
        if (array[i] === item)
          return i;
      }
      return -1;
    }
    indexOf(array, item);               
    //ie9+
    array.indexOf(item);
#### 循环监听
    var mydivs = document.getElementById("box").getElementsByTagName("div");
    for(var i = 0;i<=mydivs.length;i++){
        mydivs[i].no = i;
        mydivs[i].onclick = function(){
            console.log('我是第' + this.no + '个');
    }
## 事件类
#### 事件委托
    (function(){
        var resources = document.getElementById('resources');
        resources.addEventListener('click',handler,false);
        function handler(e){
            var x = e.target; // get the link tha
            if(x.nodeName.toLowerCase() === 'a'){
                alert('Event delegation:' + x);
                e.preventDefault();
            }
        };
    })();
## 模块化
#### 匿名函数和模块化
    //方法一
    var myApplication = function(){
        var name = 'Chris';
        var age = '34';
        var status = 'single';
        function createMember(){
            // [...]
        }
        function getMemberDetails(){
            // [...]
        }
        return{
            create:createMember,
            get:getMemberDetails
        }
    }();
    //现在写成 myApplication.get()和 
    //myApplication.create() 就行了。
    
    //方法二
    var module1 = (function(){
        var _count = 0;
        var m1 = function(){
        //...
        };
        var m2 = function(){
            //...
        };
        return {
            m1 : m1,
            m2 : m2
        };
    })();
#### js对象字面量
    var literal = {
        add: function(){
            alert("add");
        },
        del: function(){
            alert("delete");
        },
        update: function(){
            alert("update");
        },
        name: "zhangsan",
        callLiteral: function(){
            // 对于当前字面量对象的调用，要加this关键字
            this.add();
        }
    };

    //拿js对象字面量可以用 for(变量 in 对象) 
    <div id="demo">
         
    </div>
    <p>
        <script type="text/javascript">
            var mycars ={a:"a1",b:"b1",c:"c1",d:"d1"};
            var str='{a:"a1",b:"b1",c:"c1",d:"d1"}';
            var temp="";
            for (x in mycars)
            {
                temp+="数组索引或对象属性："+x+" 对应的值："+mycars[x]+"<br/>";
            }
            document.getElementById("demo").innerHTML=str+"<br/>"+temp;
        </script>
    </p>
## class相关
#### 原生js class增删
    <style type="text/css">
        div.testClass{
            background-color:gray;
        }
    </style>
    <script type="text/javascript">
        function hasClass(obj, cls) {
            return obj.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
        }

        function addClass(obj, cls) {
            if (!this.hasClass(obj, cls)) obj.className += " " + cls;
        }

        function removeClass(obj, cls) {
            if (hasClass(obj, cls)) {
                var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
                obj.className = obj.className.replace(reg, ' ');
            }
        }

        function toggleClass(obj,cls){
            if(hasClass(obj,cls)){
                removeClass(obj, cls);
            }else{
                addClass(obj, cls);
            }
        }

        function toggleClassTest(){
            var obj = document. getElementById('test');
            toggleClass(obj,"testClass");
        }
    </script>
    <body>
        <div id = "test" style = "width:250px;height:100px;">
            sssssssssssss
        </div>
        <input type = "button" value = "toggleClassTest" onclick = "toggleClassTest();" />
    </body>
## css相关
#### 获取css样式
出处：[http://www.csshello.com/jcjs/352.html](http://www.csshello.com/jcjs/352.html)
样式呢，如果直接写在行内，也就是内联样式，js能直接获取到。如果写在非行内，改怎么获取呢？
顺便科普下，总共有三种分类：内联样式(Inline Style)、内部样式表(Internal Style Sheet)和外部样式表(External Style Sheet)。
直接上代码：
- div1为行内样式
- div2为非行内样式
css部分

	#div2{width:200px; height:200px; background:red;}
html部分

	<div id='div1' style='width:200px; height:200px; background:red;'></div>
	<div id='div2'></div>
js部分

	window.onload=function(){
	   var odiv1=document.getElementById('div1');
	   var odiv2=document.getElementById('div2');
	   //由于ie不支持console.log(),故测试ie时，请使用alert()
	   console.log('行内样式获取'+odiv1.style.width);
	   console.log('非行内样式获取'+odiv2.style.width);
	   console.log('非行内样式获取通过函数'+getStyle(odiv2,'width'));
	}
	function getStyle(obj,name){
	if(obj.currentStyle){
	    //IE
	    return obj.currentStyle[name];
	}else{
	    //FF、Chrome
	    return getComputedStyle(obj,false)[name];
	}
	};

## 其他零散

### 一次弹框

	function getCookie(name) {
		var cookiefound = false
		var start = 0
		var end = 0
		var cookiestring = document.cookie;
		var i = 0;
		while (i <= cookiestring.length) {
			start = i
			end = start + name.length
			if (cookiestring.substring(start, end) == name) {
				cookiefound = true;
				break;
			}
			i++;
		}
		if (cookiefound == true) {
			start = end + 1;
			end = cookiestring.indexOf(";", start);
			if (end < start) {
				end = cookiestring.length;
			}
			return cookiestring.substring(start, end);
		}
		return "";
	}

	function newcookie(id, value, guoqi) {
		var expires = new Date()
		expires.setTime(expires.getTime() + 24 * 60 * 60 * 30 * 1000) //30为天数，可改为任意数字
		var expiryDate = expires.toGMTString();
		document.cookie = id + "=" + value + ";expires=" + expiryDate
	}

	if (getCookie("Alerted") == "") {
		alert("弹出了")
		newcookie("Alerted", "yes")
	} else {} < /script>	
***
收工！

