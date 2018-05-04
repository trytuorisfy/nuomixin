---
title: vue相同组件复用保存数据
date: 2018-05-04 14:39:26
tags: 前端
---

简单粗暴贴代码，重点是用了Object.assign()

<!--more-->

整体思路：
	listWrap通过不同的路径确认显示列表或详情。
	详情中的input框用于测试数据是否正确留存，可以将id页面上显示的id复制进去用于测试。
	详情activated时，判断是否有过值，有过则恢复，没有过则重置为初始值。beforeRouteUpdate及beforeRouteLeave时，将当期的整个data踢到父组件的对象中，已唯一id值作为判断

用vue-cli的脚手架搭了个基本页面
贴起来

	// router/index.js
	import Vue from 'vue'
	import Router from 'vue-router'
	import HelloWorld from '@/components/HelloWorld'

	Vue.use(Router)

	export default new Router({
	  routes: [
	    {
	      path: '/',
	      name: 'HelloWorld',
	      component: HelloWorld
	    },
	    {
	      path: '/list',
	      component: r => require.ensure([], () => r(require('../page/List/ListWrap')), 'ListWarp'),
	      children: [
	          {
	              path: 'all',
	              component: r => require.ensure([], () => r(require('../page/List/List')), 'List'),
	          },
				{
		      path: '/list/:id',
		      component: r => require.ensure([], () => r(require('../page/List/Detail')), 'Detail')
		    },
	      ]
	    }
	    
	  ]
	})

	//listWrap.vue
	<template>
	  <div>
	    <p>我是listwrap</p>
	    <ul>
	      <li>
	        <router-link :to="'/list/all'">all</router-link>
	      </li>
	    </ul>
	    <div>
	      <keep-alive>
	        <router-view></router-view>
	      </keep-alive>
	    </div>
	  </div>
	</template>

	<script>
	export default {
	  name: 'List',
	  components: {

	  },
	  data () {
	    return {
	      tabData:[],
	      keptData:{}
	    }
	  },
	  mounted(){

	  },
	  computed: {

	  },
	  methods:{
	  },
	  props:[]
	}
	</script>

	<!-- Add "scoped" attribute to limit CSS to this component only -->
	<style scoped>

	</style>


	// list.vue
	<template>
	  <div>
	    <p>我是list</p>
	    <ul>
	      <li v-for="item in listData">
	        <p>姓名:
	          <!-- <router-link :to="'/list/' + item.id">{{ item.name }}</router-link> -->
	          <span @click="changeTab(item.id)">{{ item.name }}</span>
	        </p>
	      </li>
	    </ul>
	  </div>
	</template>

	<script>
	export default {
	  name: 'List',
	  components: {

	  },
	  data () {
	    return {
	      listData: []
	    }
	  },
	  mounted(){
	    this.getListData()
	  },
	  computed: {
	    // demo:function(){
	    //   return ''
	    // }
	  },
	  methods:{
	    getListData(){
	      let data = [
	        {
	          "id": "5aebce8e739c96e54f825a65",
	          "guid": "0e9f4a92-844a-429c-bbd2-e89755ef68d2",
	          "name": "Lorene"
	        },
	        {
	          "id": "5aebce8ef5d7092359d8e01e",
	          "guid": "8aaf7d2e-e959-4e02-bfb6-da7154f72dea",
	          "name": "Elma"
	        },
	        {
	          "id": "5aebce8e3a80cefa24e3de06",
	          "guid": "7e4f0acc-2635-4bc9-aeae-430c5d217310",
	          "name": "Hamilton"
	        },
	        {
	          "id": "5aebce8ea5670481982ff9be",
	          "guid": "8b7f5641-0e1d-4c0f-898d-64dd14c10ef4",
	          "name": "Alisha"
	        },
	        {
	          "id": "5aebce8e9487a646c5435662",
	          "guid": "c3fdfd5f-3d99-4bc4-8c2a-4216411bbb8f",
	          "name": "Mcfadden"
	        },
	        {
	          "id": "5aebce8e6e2cd977e78b15a3",
	          "guid": "1bd8fc09-070e-4f69-be32-e4dd71c06ebc",
	          "name": "Burke"
	        }
	      ]
	      this.listData = data;

	    },
	    changeTab(id){
	      this.$router.push({ path: `/list/${id}` })
	    }
	  },
	  props:[]
	}
	</script>

	<!-- Add "scoped" attribute to limit CSS to this component only -->
	<style scoped>

	</style>

	//Detail.vue
	<template>
	  <div>
	    <p>大家好，我是{{$route.params.id}}</p>
	    <div>
	      <p>内容区</p>
	      <div>
	        {{ msg }}
	      </div>
	      <div>
	        <input type="text" v-model="iptVal">
	      </div>
	      <ul>
	        <li v-for="item in arry">{{ item }}</li>
	      </ul>
	    </div>
	  </div>
	</template>

	<script>
	export default {
	  name: 'Detail',
	  components: {

	  }, 
	  data () {
	    return {
	      msg: 'yyy',
	      iptVal:'',
	      arry:[]
	    }
	  },
	  mounted(){
	    this.getData()
	    console.log(this.$data)
	  },
	  activated(){
	    console.log('activated')
	    this.getData()
	    let id = this.$route.params.id;
	    if(this.$parent.keptData[id]){
	      console.log('有值恢复')
	      Object.assign(this.$data, this.$parent.keptData[id]);
	    }else{
	      console.log('无值获取')
	      //先重置所有值
	      Object.assign(this.$data, this.$options.data.call(this));
	      this.getData()
	    }
	    console.log(this.$parent.keptData)
	  },
	  beforeRouteUpdate (to, from, next) {
	    let id = this.$route.params.id;
	    let data = {}
	    Object.assign(data,this.$data); 
	    this.$parent.keptData[id] = data
	    next()
	  },
	  beforeRouteLeave (to, from, next) {
	    let id = this.$route.params.id;
	    let data = {}
	    Object.assign(data,this.$data); 
	    this.$parent.keptData[id] = data
	    next()
	  },
	  computed: {

	  },
	  methods:{
	    getData(){
	      let arry = [];
	      for (let i = 0; i < 10; i++) {
	        arry.push(Math.floor(Math.random()*10))
	      }
	      this.arry = arry;
	    },
	    copyArr(arr){
	        return arr.map((e)=>{
	            if(typeof e === 'object'){
	                return Object.assign({},e)
	            }else{
	                return e
	            }
	        })
	    }
	  },
	  props:[]
	}
	</script>

	<!-- Add "scoped" attribute to limit CSS to this component only -->
	<style scoped>

	</style>
