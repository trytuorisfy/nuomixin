title: 各种tips
date: 2015-07-22 11:12:57
tags: tips
---

各种零零散散的小内容，反正啥都有，都扔里面了咯~
<!--more-->
# git
找到个简单明了的[教程](http://rogerdudler.github.io/git-guide/index.zh.html)，可以来一发
前两天看到一个特别萌的教程，叫“[猴子都能懂的GIT入门](https://backlog.com/git-tutorial/cn/)”，这世道啊，猴子都比我聪明 orz
让windows Git设置为大小写敏感的命令如下

	git config core.ignorecase false 

提交时文件大小受到限制

	git config http.postBuffer 524288000

github添加ssh

- "Git Bash" 
- 键入命令：
	ssh-keygen -t rsa -C "email@email.com"
- 用记事本打开id_rsa.pub文件，复制内容，到github网站上到ssh密钥管理页面，添加新公钥，随便取个名字，黏贴内容

需要注意产生的密钥文件在当前用户的根目录，必须把这两个文件放到当前用户目录的“.ssh”目录下才能生效。如C:\Users\xxx\.ssh

## git提交相关

查看当前状态  git status

### git merge
将A分支合并到B分支
git checkout B
git merge A

### [git stash](https://git-scm.com/book/zh/v1/Git-%E5%B7%A5%E5%85%B7-%E5%82%A8%E8%97%8F%EF%BC%88Stashing%EF%BC%89)
1.git stash
2.git stash list
3.git stash apply
4.git stash drop stash@{0} //丢掉制定的储藏
5.git stash pop //重新应用储藏并移走

### [git cherry-pick](http://www.jianshu.com/p/08c3f1804b36)
从分支A中取需要的内容到分支B
分支A中：
git log //拿到commit的编号
git checkout B

分支B中：
git cherry-pick A中拿到的编号

如果有冲突，手动修改后
git add xx/xxx.js
git commit -m 'commit内容'

其他参数 git cherry-pick --continue/quit/abort   //玩坏了就用abort

[官方地址](https://git-scm.com/docs/git-cherry-pick)

## [.gitignore](http://www.jianshu.com/p/e5b13480479b)
项目里有个打包生成的dist文件夹，本来也没啥，然后要开分支，要同步，然后就懵逼了，想想总改dist文件夹里面的文件总不是个事吧，这不是找事吗，然后搜索了一把，可以用.gitignore解决，我不跟踪你还不行吗

1.git rm -r --cached 要忽略的文件  //我这就是dist文件夹 git rm -r --cached dist/*  全部不要 git rm -r --cached .
2.git add .
3.git commit -m 'commit内容'
4.git push




# mui
让a链接点击后能跳转

	mui('.mui-bar-tab').on('tap','a',function(){document.location.href=this.href;});

遮罩蒙版相关

	//js部分
	var mask = mui.createMask(callback);//callback为用户点击蒙版时自动执行的回调；
	mask.show();//显示遮罩
	mask.close();//关闭遮罩

	//css部分
	.mui-backdrop {
	    position: fixed;
	    top: 0;
	    right: 0;
	    bottom: 0;
	    left: 0;
	    z-index: 998;
	    background-color: rgba(0,0,0,.3);
	}

scroll(区域滚动)

	//html部分
	<div class="mui-scroll-wrapper">
		<div class="mui-scroll">
			<!--这里放置真实显示的DOM内容-->
		</div>
	</div>
	//js部分
	mui('.mui-scroll-wrapper').scroll({
		deceleration: 0.0005 //flick 减速系数，系数越大，滚动速度越慢，滚动距离越小，默认值0.0006
	});
	//滚到顶部
	mui('.mui-scroll-wrapper').scroll().scrollTo(0,0,100);//100毫秒滚动到顶
	//滚动底部
	mui('.mui-scroll-wrapper').scrollToBottom(100)

元素选取及时间
	
	//元素
	//mui使用css选择器获取HTML元素，返回mui对象数组。
	//mui("p")：选取所有<p>元素
	//mui("p.title")：选取所有包含.title类的<p>元素

	//obj1是mui对象
	var obj1 = mui("#title");
	//obj2是dom对象
	var obj2 = obj1[0]; 

	//事件
	除了可以使用addEeventListener()方法监听某个特定元素上的事件外， 也可以使用.on()方法实现批量元素的事件绑定	
	.on( event , selector , handler ) 
	点击 	
	tap 		单击屏幕
	doubletap 	双击屏幕
	长按 	
	longtap 	长按屏幕
	hold 		按住屏幕
	release 	离开屏幕
	滑动 	
	swipeleft 	向左滑动
	swiperight 	向右滑动
	swipeup 	向上滑动
	swipedown 	向下滑动
	拖动 	
	dragstart 	开始拖动
	drag 		拖动中
	dragend 	拖动结束

最后上一段示例中的js

	<script src="js/mui.min.js"></script>
	<script>
		mui.init();

		/*mui js示范 和此部分内容无关*/
		(function($) {
			$('#scroll').scroll({
				indicators: true //是否显示滚动条
			});
			var segmentedControl = document.getElementById('segmentedControl');
			$('.mui-input-group').on('change', 'input', function() {
				if (this.checked) {
					var styleEl = document.querySelector('input[name="style"]:checked');
					var colorEl = document.querySelector('input[name="color"]:checked');
					if (styleEl && colorEl) {
						var style = styleEl.value;
						var color = colorEl.value;
						segmentedControl.className = 'mui-segmented-control' + (style ? (' mui-segmented-control-' + style) : '') + ' mui-segmented-control-' + color;
					}
				}
			});
		})(mui);
	</script>

# Bootstrap相关
### admin主题
[AdminLTE](https://github.com/almasaeed2010/AdminLTE)


# 零散知识点
### 空格
	&nbsp; // space 不叠加
	&ensp; // 1/2个中文宽度
	&emsp; // 1个中文宽度

### [判断ios版本](http://blog.sina.com.cn/s/blog_56e3129d0101l2xx.html)

       alert(Boolean(navigator.userAgent.match(/OS [9]_\d[_\d]* like Mac OS X/i))) //返回值为true是ios9


	   function gt_ios4() {
	    // 判断是否 iPhone 或者 iPod
	    if((navigator.userAgent.match(/iPhone/i) || navigator.userAgent.match(/iPod/i))) {
	        // 判断系统版本号是否大于 4
	        return Boolean(navigator.userAgent.match(/OS [5-9]_\d[_\d]* like Mac OS X/i));
	    } else {
	        return false;
	    }
	}

### [css判断iphone](http://www.phptext.net/article_view.php?id=387)

### 元素垂直居中

	//css 如果样式有问题，则需要加前缀如   -webkit-transform:translate(-50%,-50%);
	position:absolute; top:50%;left:50%;transform:translate(-50%,-50%); 

### 小图标与文字对齐，来自[张鑫旭的博客](http://www.zhangxinxu.com/wordpress/2016/03/css-layout-base-20px/)

	//html 图标中是否有文字都可以
	<i class="icon"></i>
	<a href="javascript:" class="icon">删除</a>
	//css
	.icon { 
	    display: inline-block; 
	    width:20px; height:20px; 
	    background: ...; 
	    white-space:nowrap; 
	    letter-spacing: -1em; 
	    text-indent: -99em; 
	    color: transparent;
	    /* IE7 */
	    *text-indent: 0;
	    *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '\3000');
	}
	.icon:before {
	    /* 伪元素插入空格文本 */
	    content: '\3000'; 
	}
### 字符串转数组
	
	//吐槽先 虽然你长的像数组，但是残酷的现实告诉我，你只是长得像... [5, 4, 2, 3, 6]
    var iphone_str = "[5, 4, 2, 3, 6]";
    iphone_arr = iphone_str.replace("[","").replace("]","").replace(/ /g,"").split(',');//replace(/ /g,"") 替换全部空格
    console.log(iphone_arr);
    for (var i = 0; i < iphone_arr.length; i++) {
        $('#iphone-pieces').find('.iphone-piece').eq(iphone_arr[i]-1).addClass('piece-visible');
    };	

### 字符串分割指定长度并插入字符

    changeStrTT:function(str,len){ //str为目标string, len为期望分割的长度
        if(str==null||str==""){
            return "";
        }
        if(len==null){
            len=10;
        }
        var result="";
        var curlen=0;
        var patten= /.*[\u4e00-\u9fa5]+.*$/;
        for(var i=0;i<str.length;i++){
            if(patten.test(str[i])){
                curlen+=2;
            }else{
                curlen++;
            }
            if(curlen>=len){
                curlen=0;
                // result+="\n";
                result+="<br>";
            }
            result+=str[i];
        }
        return result;
    }

### JSON.parse()和JSON.stringify()

	var str = '{"first":"firstcont","second":"secondcont"}';
	JSON.parse(str); //string转object
	var obj = {a:1,b:2};
	JSON.stringify(obj); //object转string

### 组成数据来一发
[参考来源](http://www.111cn.net/wy/js-ajax/44050.htm)
实际用到的地方，用for循环整一个数组出来

	//anotherArry就是另外的数组了
    var myArry = new Array();
    for (var i = 0; i < anotherArry.length; i++) {
        var fieldlabel = anotherArry[i].fieldLabel;
        var value = anotherArry[i].value;
        myArry[fieldlabel] = value;
    }

### 修改checkbox样式
[参考来源](https://segmentfault.com/q/1010000002547288)
	
	//html
	<label>
	    <input type="checkbox" class="hidden-input" />
	    <span class="your style about checkbox"></span>
	    记住我
	</label>
	.hidden-input {
	    opacity: 0;
	    position: absolute;
	    z-index: -1;
	}
	
	//css
	input[type=checkbox]+span {
	    /* your style goes here */
	    display: inline-block;
	    height: 1em;
	    width: 1em;
	    border-radius: 4px;
	    background-color: gray;        
	}
	/* active style goes here */
	input[type=checkbox]:checked+span {
	    background-color: red;
	}


### [Django Built-in template tags and filters](https://docs.djangoproject.com/en/dev/ref/templates/builtins/)

	//比较实用的是blocktrans，自行搜索
### [判断元素是否在可见窗口范围内](http://www.cnblogs.com/kevinge/p/3937084.html)

    <div style="width:1px;height:2000px;"></div>
    <div id="eq" style=" width:100px; height:100px; background-color:Red;">1</div>
    <div style="width:1px;height:2000px;"></div>
    <script src="http://code.jquery.com/jquery-latest.js" type="text/javascript"></script>
    <script type="text/javascript">
        $(document).ready(function () {
            $(window).scroll(function () {
                var a = document.getElementById("eq").offsetTop;
                if (a >= $(window).scrollTop() && a < ($(window).scrollTop()+$(window).height())) {
                    console.log("div在可视范围");
                }else{
                    console.log('看不见哟看不见')
                }
            });
        });
    </script>

### 判断浏览器语言

	//判断浏览器语言
	var language = navigator.browserLanguage?navigator.browserLanguage:navigator.language; 
	if (language.indexOf('en') > -1){document.location.href = 'index.html'; }
	else if (language.indexOf('ar') > -1){ document.location.href = 'index_ar.html'; }  //阿拉伯语
	else if (language.indexOf('ru') > -1){ document.location.href = 'index_ru.html'; }  //俄罗斯语
	else if (language.indexOf('es') > -1){ document.location.href = 'index_es.html'; }  //西班牙语
	else if (language.indexOf('it') > -1){ document.location.href = 'index_it.html'; }  //意大利语
	else if (language.indexOf('nl') > -1){ document.location.href = 'index_nl.html'; }  //荷兰语
	else if (language.indexOf('pt') > -1){ document.location.href = 'index_pt.html'; }  //葡萄牙语
	else {}

### 用canvas画的行星轨道图
	[地址戳下哟](http://www.pengyaou.com/codecss3/POKDNMS_9.html)
	


### 各种零散小知识
- [获取图片尺寸](http://www.qttc.net/201304304.html)
- [css3做的优惠券](http://www.daqianduan.com/5989.html)
- [Django模板](http://raytaylorlin.com/Tech/Script/Python/django-note-3/)

# 奇葩的bug
此版块用于吐槽真正好,我那心情啊...

### 谷歌广告不显示
	谷歌广告放在js生成的html中，结果就是不显示。我那心情...
	解决方法：
	在html文件中，先放一段谷歌广告（display:none）隐藏掉，然后其他广告就显示了...

# 踩过的坑
总有一些坑，让我踩一踩o(╯□╰)o
## 数组相关
		
		//以下方法主要用于在for循环时，给数组增加key和value
		var testArry = {}; //嘿嘿嘿 如果写成这样 var testArry = new Array();  jjj就是个空值！
		testArry['lala'] = 'yoyo';
		testArry['lalwera'] = 'y345oyo';
		testArry['lalewr4a'] = 'yoy8yo';
		testArry['lal45a'] = 'yo678yo';
		console.log(testArry)
		var jjj = JSON.stringify(testArry)
		console.log(jjj) 
## [json显示在页面上](http://jsfiddle.net/KJQ9K/554/)
关键是用了JSON.stringify(),[可参考](http://www.cnblogs.com/damonlan/archive/2012/03/13/2394787.html)
保险起见，让我抄一遍 

	//js
	function output(inp) {
	    document.body.appendChild(document.createElement('pre')).innerHTML = inp;
	}

	function syntaxHighlight(json) {
	    json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
	    return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
	        var cls = 'number';
	        if (/^"/.test(match)) {
	            if (/:$/.test(match)) {
	                cls = 'key';
	            } else {
	                cls = 'string';
	            }
	        } else if (/true|false/.test(match)) {
	            cls = 'boolean';
	        } else if (/null/.test(match)) {
	            cls = 'null';
	        }
	        return '<span class="' + cls + '">' + match + '</span>';
	    });
	}

	var obj = {a:1, 'b':'foo', c:[false,'false',null, 'null', {d:{e:1.3e5,f:'1.3e5'}}]};
	var str = JSON.stringify(obj, undefined, 4);

	output(str);
	output(syntaxHighlight(str));
	//css
	pre {outline: 1px solid #ccc; padding: 5px; margin: 5px; }
	.string { color: green; }
	.number { color: darkorange; }
	.boolean { color: blue; }
	.null { color: magenta; }
	.key { color: red; }











