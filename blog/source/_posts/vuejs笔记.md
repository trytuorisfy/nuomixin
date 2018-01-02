title: vuejs笔记
date: 2016-02-26 11:09:01
tags: 笔记
---
# [概览](http://blog.evanyou.me/2015/10/25/vuejs-re-introduction/)
<!--more-->
# 实用
## 基础模板
    var object = {
      message: 'Hello world!'
    }
    <div id="example">
      {{ message }}
    </div>
    new Vue({
      el: '#example',
      data: object
    })

## [http请求插件vue-resource](https://github.com/vuejs/vue-resource)
## [vue-cli](https://github.com/vuejs/vue-cli)

    $ npm install -g vue-cli
    $ vue init webpack my-project
    $ cd my-project
    $ npm install
    $ npm run dev
    $ npm run build

#重点是坑！！！
## 兄弟关系
曾经我天真的以为兄弟关系是确定的，结果太打脸了，chrome那边兄弟关系是对的，看下Firefox竟然不对了，大儿子突然就变小儿子了，我的心哇凉哇凉的。只要用到兄弟关系查找元素的都歇菜了！
于是，机智的我只能放大招了！ 在new Vue的时候，直接把所有关系算出来赋值！哼！ 用的时候直接用  this.$root.xxxIndex 这种形式来找到序号。上个示例吧还是,假设根元素下面有2个子元素

    //定义component
    Vue.component('first-comp',{
      template:'#first-temp',
      data:function(){
        return {
          compName:'first'
        }
      },
      methods:{
        test:function(){
          console.log('test')
        }
      }
    })
    Vue.component('second-comp',{
      template:'#second-temp',
      data:function(){
        return {
          compName:'second'
        }
      }
    })  
    //new Vue
    new Vue({
      el: '#body-wrap',
      data: {
          firstIndex:'',
          secondIndex:'',
      },
      ready:function(){
          if(this.$root.$children[0].compName == 'first'){
              this.firstIndex = 0;
              this.secondIndex = 1;
          }else{
              this.firstIndex = 1;
              this.secondIndex = 0;           
          }
      }
    })
    //调用方法示例
    this.$root.$children[firstIndex].test();
    //补充：今天又看了文档，发现这个问题的解决方法是这样的[v-ref](http://vuejs.org.cn/api/#v-ref)
    //template
    <comp v-ref:child></comp>
    <comp v-ref:some-child></comp>
    // 从父组件访问
    this.$refs.child
    this.$refs.someChild

## 页面里的正则
由于本人脑子小，要在v-for循环出来的数据里替换 &gt ; &lt ;(无视中间的空格) 为 > 和 < ,那其中的辛酸哎哟都不想提起，最后解决方案是：
把正则作为一个值放在js中,如下

    //js
    data:function(){
      return {
        regExpGt:/&gt;/g,
        regExplt:/&lt;/g          
      }
    }    
    //html 编译问题 以下中文自己替换
    <li v-for='value in items'>双花括号 value.replace(regExpGt,'>').replace(regExplt,'<') 双花括号</li>




# 来个模板
[vuejs-templates/browserify](https://github.com/vuejs-templates/browserify)
嘿嘿嘿，整个文件就是.vue,把html，css，js都放在里面了，刚试了一下，我只想说，你的语法要不要这么严格！！！空格不能多也不能少，分号再见。
还有一个很奇怪的就是，我把需要的东西放在static文件夹中，才访问的到。虽然我觉得应该是要放到src/assets这个文件夹的，但是地址总是写不对，总是404，没办法才想了其他办法，可以放static文件夹中没问题了，就先放着吧。
抄写几段实用的(只抄了js部分)：
    
    //Hello.vue
    <script>
    export default {
      data () {
        return {
          // note: changing this line won't causes changes
          // with hot-reload because the reloaded component
          // preserves its current state and we are modifying
          // its initial state.
          msg: 'Hello World!',
          otherData: ''
        }
      },
      ready () {//看清楚这里，和直接写在js里的写法不一样，空格注意！空格严格按照它的来空，不然你被报错刷屏了
        var url = './static/addrule.json'
        this.$http.get(url).then(function (response) {//空格注意！
          var data = response.data
          console.log(data)
          this.listData = data
        }, function (response) {//空格注意！

        })
      }
    }
    </script> 
    //App.vue
    <script>
    import Hello from './components/Hello'

    export default {
      components: {
        Hello
      }
    }
    </script>    
    //main.js
    import Vue from 'vue'
    import App from './App'
    Vue.use(require('vue-resource')) //亮点看这里，这个插件是ajax的插件哟

    /* eslint-disable no-new */
    new Vue({
      el: 'body',
      components: { App }
    })





# 一些tips
- [列表渲染 不能检测到如下变化：](http://cn.vuejs.org/guide/list.html)
    直接用索引设置元素，如 vm.items[0] = {}；
    修改数据的长度，如 vm.items.length = 0。
  解决方法：
    example1.items.$set(0, { childMsg: 'Changed!'}) // 快捷的$remove()方法：this.items.$remove(item)
    至于问题 (2)，只需用一个空数组替换 items
- 可以通过将 vm.$data 传入 JSON.parse(JSON.stringify(...)) 得到原始数据对象。[链接](http://cn.vuejs.org/api/#data)
- [父子组件通信](http://cn.vuejs.org/guide/components.html#父子组件通信)
  子组件可以用 this.$parent 访问它的父组件。根实例的后代可以用 this.$root 访问它。父组件有一个数组 this.$children，包含它所有的子元素




