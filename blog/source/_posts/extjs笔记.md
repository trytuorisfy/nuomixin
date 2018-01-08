title: ext.js v6.0笔记
date: 2016-02-04 09:33:44
tags: 笔记
---
记性不好的人啊，还是写下来吧。
# 安装
- 安装[senchacmd](https://www.sencha.com/products/extjs/cmd-download/)
- 安装[ruby](http://www.ruby-lang.org/en/downloads/)
- 下载[ext.js](http://extjs.org.cn/node/764),这里是ExtJS 6.0.0 GPL开源版。吐个槽，文档里总是会提到sdk，然后后面我猜发现sdk指的就是下载下来的压缩包，我那心情啊。
- sencha -sdk /path/to/ext6 generate app MyApp /path/to/my-app
	示例：sencha -sdk /path/to/ExtSDK generate app -classic TutorialApp ./TutorialApp
- 进入目标目录 sencha app watch，页面显示地址为 http://localhost:1841
- 桌面的内容在 classic文件夹 
    classic/src/main/main.js入口
    classic/sass/src/ 里面修改sass文件改样式
- 入口 根目录 app.js 其中规定了最开始进入的页面

<!--more-->

# 笔记内容开始
## 注意点：
### 命名
    The top-level namespaces and the actual class names should be CamelCased. Everything else should be all lower-cased. For example:MyCompany.form.action.AutoLoad
    path/to/src is the directory of your application’s classespath/to/src is the directory of your application’s classes
    Acceptable method names:encodeUsingMd5()
    Acceptable variable names:var isGoodName

### 声明
    Ext.define(className, members, onClassCreated);
### 获取值
Ext.define()中的Config中的值可以用getXxx,setXxx来获取，注意[驼峰命名](http://docs.sencha.com/extjs/6.0/core_concepts/classes.html)

    config: {
       title: 'Title Here',
       bottomBar: {
           height: 50,
           resizable: false
       }
    }


## 技能
### [加上事件](http://docs.sencha.com/extjs/6.0/core_concepts/events.html)
下面例子就加上了click事件

    var container = Ext.create('Ext.Container', {
        renderTo: Ext.getBody(),
        html: 'Click Me!',
        listeners: {
            click: function(){
                Ext.Msg.alert('I have been clicked!')  
            }
        }
    });
    container.getEl().on('click', function(){ 
        this.fireEvent('click', container); 
    }, container);

### widget not found

    sencha app build

以上是打包的命令，运行后在build文件夹中会有production文件夹，东西都在那里面。
进去找到index.html点开后，如果报错，列如 widget/tabpanel.js 404 not found这种，那就找到用到tabpanel的地方，一般是因为你 xtype:tabpanel 这种地方，然后在相应的文件中，require下对应的名称即可，以[tabpanel](http://docs.sencha.com/extjs/6.0/6.0.0-classic/#!/api/Ext.tab.Panel)为例,requier写法如下：

    requires: [
        'Ext.container.Container',
        'Ext.tab.Panel', //看这里！对就这里，这个值怎么查到的呢，很简单，就是xtype:tabpanel对应的那个名字啦(查官方文档)
        'Ext.form.field.File'
    ],

# 通用方法
## 查找元素[ext.componentquery](http://docs.sencha.com/extjs/6.0/6.0.0-classic/#!/api/Ext.ComponentQuery)
    我这智商，找了好久 orz

    var myPanel = Ext.ComponentQuery.query('#myPanel'); 
    //实际使用过程中，需要写成这样才能真正拿到这个组件
    myPanel[0]


# 具体项目
## [grid](http://docs.sencha.com/extjs/6.0/6.0.0-classic/#!/api/Ext.grid.Panel)相关
### 表格不要隔行变色，[属性竟然藏在这里viewConfig](http://docs.sencha.com/extjs/6.0/6.0.0-classic/#!/api/Ext.view.Table)

    viewConfig: {
        stripeRows: false
    }
    
### 表格多选行

    //配置
    selModel: {
        selType: 'cellmodel',
        mode   : 'MULTI' //多选
    }
    //方法
    getSelection()

### 表格中的内容无法选中解决方法
    这个大腿必须抱啊！[看这里](http://blog.csdn.net/yeshigudu/article/details/48522239)！！救人于水火啊！！！

    viewConfig: {
        enableTextSelection: true
    }

### [高亮行](https://www.sencha.com/forum/showthread.php?140274-grid-row-selection-in-ExtJS4),
    [取消高亮](http://forums.ext.net/showthread.php?868-CLOSED-Clearing-selection-from-a-gridpanel)
反正就是一把辛酸的泪，那些没设置延时的，你们怎么成功实现高亮的！！！
上结果：

    var urlListTab = Ext.ComponentQuery.query('#urlListTab')[0];
    setTimeout(function() {urlListTab.getSelectionModel().select(index, false, false)}, 800); //
    index为行的index值。第一个false时，进入这个grid时，有其他的高亮行时，指定的这行就不亮了，这个就看看，实际用的时候再测测
    //清除高亮
    GridPanel1.getSelectionModel().clearSelections //当前高亮全部去除

## [tab](http://docs.sencha.com/extjs/6.0.0-classic/Ext.tab.Panel.html)
我只是简单的想隐藏个tab，结果智商是硬伤，官方文档里就有好不好 orz

    var tabs = Ext.create('Ext.tab.Panel', {
        width: 400,
        height: 400,
        renderTo: document.body,
        items: [{
            title: 'Home',
            html: 'Home',
            itemId: 'home' // 看这里!!! 是itemId,不是id!!!
        }, {
            title: 'Users',
            html: 'Users',
            itemId: 'users',
            hidden: true
        }, {
            title: 'Tickets',
            html: 'Tickets',
            itemId: 'tickets'
        }]
    });

    Ext.defer(function(){
        tabs.child('#home').tab.hide();
        var users = tabs.child('#users');
        users.tab.show();
        tabs.setActiveTab(users);
    }, 1000);

## [store](http://docs.sencha.com/extjs/6.0/6.0.0-classic/#!/api/Ext.data.Store)和[storeManager](http://docs.sencha.com/extjs/6.0/6.0.0-classic/#!/api/Ext.data.StoreManager)
先吐槽，store的水好深（其实我好想打三个点，但我要忍住）
### 拿到store

    Ext.create('Ext.data.Store', {
        model: 'SomeModel',
        storeId: 'myStore'
    });
    var store = Ext.data.StoreManager.lookup('myStore');//用storeId拿到

### 用store
    
    Ext.create('Ext.data.Store', {
        model: 'SomeModel',
        storeId: 'myStore'
    });
    Ext.create('Ext.view.View', {
        store: 'myStore', //用storeId就到手啦，真好
        // other configuration here
    });

### [store具体方法](http://docs.sencha.com/extjs/6.0/6.0.0-classic/#!/api/Ext.data.Store)
    
    //特别提醒，先要拿到store，说多了都是泪
    //增加内容
    myStore.add({some: 'data'}, {some: 'other data'});
    myStore.insert(index, records); //eg: myStore.insert(0, { "name": "hello", "age": "60"})  
    myStore.find('name', 'hello'); //返回的是序列号，即index
    myStore.removeAt( index, [count] ) //嘿嘿嘿，拿到序号就可以删除啦


## data
### [field](http://docs.sencha.com/extjs/6.0/6.0.0-classic/#!/api/Ext.data.field.Field)
在这里可以重组field的数据

    {
        name: 'firstName',
        convert: function (value, record) {
            return record.get('name').split(' ')[0];
        },
        depends: [ 'name' ]
    }

### [data.model](http://docs.sencha.com/extjs/6.0/6.0.0-classic/#!/api/Ext.data.Model)
绑定数据相关，好好看看

## ajax相关
我一定要写下来，最后我都把我自己感动了，太不容易了，拿个值。
[Ext.ajax](http://docs.sencha.com/extjs/6.0/6.0.0-classic/#!/api/Ext.Ajax)

    Ext.define('ttt', function() {
         return{
            getData:function(){
                var userData;
                Ext.Ajax.request({
                    async: false,//就是这个地方！要加！不然return出来的是undefined
                    url: 'resources/userinfo.json',
                    success: function(response, opts) {
                        var obj = Ext.decode(response.responseText);
                        console.log('成功')
                        userData = obj;
                    },
                    failure: function(response, opts) {
                        console.log('server-side failure with status code ' + response.status);
                        userData = 'failure'
                    }
                });
                return userData;
            }
         }
    })
    var test = new ttt();
    var userData = test.getData()
    //我会说这个userData拿到了要来干嘛吗？

    //引入
    viewModel: {
        data: userData
    }
    //使用
    {
        xtype:'button',
        bind: {
            text: '{username}'//json里面有的字段就可以用啦
        },            
    }

    //正常实用款
    Ext.Ajax.request({
        url: 'resources/userinfo.json',
        success: function(response, opts) {
            var data = Ext.decode(response.responseText);
            //数据处理动起来
        },
        failure: function(response, opts) {
            console.log('server-side failure with status code ' + response.status)
        }

    });

    //亮点来啦！！ [jsonp](http://docs.sencha.com/extjs/6.0/6.0.0-classic/#!/api/Ext.data.proxy.JsonP)
    proxy: {
        type: 'jsonp',
        url : 'http://domainB.com/user',
        callbackKey: 'callback', //亮点在这里，callback=Ext.data.JsonP.callback1 “callback”此字段名一定要匹配！！！
        reader: {
            rootProperty: 'rows',
            totalProperty: 'resutls'
        }
    },

## define
我觉得挺实用的，拉出来

     Ext.define('My.awesome.Class', {
         someProperty: 'something',
         someMethod: function(s) {
             alert(s + this.someProperty);
         }
         ...
     });
     var obj = new My.awesome.Class();
     obj.someMethod('Say '); // alerts 'Say something'



## [base64](http://docs.sencha.com/extjs/6.0/6.0.0-classic/#!/api/Ext.util.Base64)
    自带！！！

    //解码
    res = Ext.util.Base64.decode(res); 

## form相关
表单提交后一直进入failure的[解决方法](http://atechiediary.blogspot.jp/2013/06/ext-js-form-submit-return-always-failure.html),就是需要在返回的json中加入一个字段{"success": true},亲测可用


