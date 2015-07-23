title: Angular.js 笔记类
date: 2015-03-23 16:21:51
tags: 前端
---

突然想到一句话特别合适
**我不生产笔记，我是笔记的搬运工...**

是到处看来的，觉得有用就记一笔，走过路过的朋友也就随便看看。
强势插入！ UI看这里！！[http://angular-ui.github.io/bootstrap/](http://angular-ui.github.io/bootstrap/)
再次强势插入！！ 终于找到了 angular.js 异步加载[https://github.com/geddski/overmind](https://github.com/geddski/overmind) 找的我真是一把辛酸的泪啊


记录些零散的小东西

[参考来源： 吕大豹（Double.Lv）](http://www.cnblogs.com/lvdabao/p/3475426.html)
### 过滤器

#### orderBy(排序)
	<div>{{ childrenArray | orderBy : 'age' }}</div>      //按age属性值进行排序，若是-age，则倒序
	<div>{{ childrenArray | orderBy : orderFunc }}</div>   //按照函数的返回值进行排序
	<div>{{ childrenArray | orderBy : ['age','name'] }}</div>  //如果age相同，按照name进行排序
吐槽： 倒叙就只要加个“-”就好了，简直太赞了！

### 零散tips
#### 图片src
	<img ng-src="{{xxx.imageUrl}}">
### 获取数据
	function PhoneListCtrl($scope, $http) {
	$http.get('phones/phones.json').success(function(data) {
		$scope.phones = data;
	});
	}
### 路由

	angular.module('phonecat', []).
	config(['$routeProvider', function($routeProvider) {
	$routeProvider.
	when('/phones', {
		templateUrl: 'partials/phone-list.html',
		controller: PhoneListCtrl
	}).
	when('/phones/:phoneId', {
		templateUrl: 'partials/phone-detail.html',
		controller: PhoneDetailCtrl
	}).
	otherwise({
		redirectTo: '/phones'
	});
	}]);

路由数据取用

	function PhoneDetailCtrl($scope, $routeParams) {
	 $scope.phoneId = $routeParams.phoneId;  //注意到在第二条路由声明中:phoneId参数的使用。$route服务使用路由声明/phones/:phoneId作为一个匹配当前URL的模板。所有以:符号声明的变量（此处变量为phones）都会被提取，然后存放在$routeParams对象中。
	}

一些骨架基础

	<html ng-app="MyApp"> //作用域
	<div ng-controller="testC"> //声明一个需要和数据进行绑定的模板区域，它的作用域就是这个div之内的东西
	<input type="radio" name="optcheck" ng-show="question.type==1" /> //ng-show用法



	var app = angular.module('MyApp', [], function(){console.log('started')}); //声明模块
	var testC = function($scope){}

	tips
	通过{{}}只能完成数据向模板的单向绑定。要想进行双向绑定，我们需要用到ng-modle这个指令

## 一些好的教程啊 笔记啥的
[流浪猫の窝 ](http://www.cnblogs.com/liulangmao/category/625051.html)强强烈推荐！！！
[好神奇 迭代的时候竟然还是first什么的 ng-repeat](http://www.cnblogs.com/liulangmao/p/3716522.html)
[css相关 就是下面的内容来源](http://www.cnblogs.com/liulangmao/p/3719085.html)

    <div class="tip" ng-class="{err:ifErr,warn:ifWarn}" ng-show="ifShow">{{tipText}}</div>
      //其中,err和warn是待选的类名,":"后面绑定数据,该数据决定了该类名是否会被添加,如果数据的值为true,该类名会被添加,反之则不会被添加
      然后通过给按钮绑定点击事件,来改变ifErr和ifWarn的布尔值,改变tip元素的类名,显示不同的提示框

###$scope
控制器可以内嵌,比如:

	<div ng-controller = "ParentController">
	  <h3>{{title}}</h3>
	  <div ng-controller = SonController>
	    <h5>{{title}}</h5>
	  <div>
	</div>

	function ParentController ($scope){
	    $scope.title = 'I am ParentController';
	}
	function SonController ($scope){
	    $scope.title = 'I am SonController';
	}

可以得到正确的视图:

	I am ParentController
	I am SonController

如果我们把这句话注释掉: 

	//$scope.title = 'I am SonController';

会得到这样的视图:

	I am ParentController
	I am ParentController


实际上,**控制器的嵌套,就是作用域的嵌套**,传递给内嵌控制器呃$scope继承了它父控制器的$scope.
所以SonController的$scope可以访问ParentController的$scope的所有属性和方法

### factory[详细戳这里](http://www.cnblogs.com/liulangmao/p/3727808.html)
直接上重点，就这么简单粗暴

	var shoppingCart = angular.module('shoppingCart',[]);
	shoppingCart.factory('Items',function(){
	    var items = {};
	    //这段数据实际应该是从数据库拉取的
	    items.query = function(){
	        return [
	            {"title":"兔子","quantity":1,"price":"100"},
	            {"title":"喵","quantity":2,"price":"200"},
	            {"title":"狗只","quantity":1,"price":"400"},
	            {"title":"仓鼠","quantity":1,"price":"300"}
	        ]
	    };
	    return items;
	});
	shoppingCart.controller('CartController',function($scope,Items){
	    $scope.items = Items.query();
	});	
### 布局和视图
    <a href="#/view/{{message.id}}"  //链接应该使用"#/..." 使用#开头表示改变路径的hash值

### 数据专场(http resource等)
$routeParams 可以获取当前路径参数.需要ngroute模块被安装。
路径参数是$location.search()和$location.path()的组合. 在参数名称冲突的情况下，路径参数优先于搜索参数

	 // URL: http://server.com/index.html#/Chapter/1/Section/2?search=moby
	 // 路由规则: /Chapter/:chapterId/Section/:sectionId
	 //
	 // 结果
	 $routeParams ==> {chapterId:'1', sectionId:'2', search:'moby'}

#### get

	$http.get('url',{}).success(function(data,status,headers,config){
	}).error(function(data,status,headers,config){
	})
 json对象: 请求参数配置,如 {params:{id:5}}，这样得到的实际路径就是url?id=5


因为data是异步返回的,必须使用$q的promise
 
	var httpGet = angular.module('HttpGet',[]);
	httpGet.factory('getData',function($http,$q){
	    return function(){
	        var defer = $q.defer();     $http.get('/api/user').success(function(data,status,headers,congfig){
	            //console.log(status);
	            //console.log(headers);
	            //console.log(congfig);
	            defer.resolve(data);
	        }).error(function(data,status,headers,congfig){
	            defer.reject(data);
	        });
	        return defer.promise
	    }
	});
	httpGet.controller('dataController',function($scope,getData){
	    $scope.data = getData()
	});
#### post
	$http.post('url',{},{}).success(function(data,status,headers,config){
	}).error(function(data,status,headers,config){
	})
1. url: 请求的路径
2. 请求发送的数据: json对象 {name:'code_bunny'}
3. 请求配置的参数: json对象 {params: {id:5}} 这样得到的实际路径就是url?id=5

		var httpGet = angular.module('HttpGet',[]);
		httpGet.factory('getData',function($http,$q){
		return function(){
		    var defer = $q.defer();
		    $http.post('/api/user',{name:'code_bunny'}).success(function(data,status,headers,congfig){
		        defer.resolve(data);
		    }).error(function(data,status,headers,congfig){
		        defer.reject(data);
		    });
		
		    return defer.promise
		}
		});
		httpGet.controller('dataController',function($scope,getData){
		$scope.data = getData()
		});	

#### ngResource
	$resource(url,{url参数},{自定义方法})
	url: 必填,资源的基础url
	url中带有 ':' 项的是根据第二个参数来进行配置的. 
	url参数: 选填,配置url中的带有 ':' 项的参数	


## 一个牛逼的教程 动态加载的 努力看！[动态加载](http://weblogs.asp.net/dwahlin/dynamically-loading-controllers-and-views-with-angularjs-and-requirejs)

***
鉴于终于找到了异步加载的插件，见再次强势插入，所以应该暂时就不加啥东西了，就发布咯~




