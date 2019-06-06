---
title: 监听hash
date: 2019-06-06 14:40:41
tags: 前端
---

避免修改url中的参数造成页面刷新，将参数全部踢到hash中。

方式一：
页面上条件选择好后，提交，把相关参数踢到hash中。

方式二：
刷新页面或带参数进入页面时，获取hash中的参数填入页面，并发起请求。


简单粗暴贴代码，用的vue


        data() {
            return {
              searchKey:'',
              state:'',
              listenHash:true //是否监听hash变化
            }
        },
        ready(){            
            this.listenHashChange();
            // 判断有没有hash值
            let hash = window.location.hash;
            if(hash){
              this.getUrlHash();
            }else{
              this.getMainData();
            }
    
        },
        methods: {
            getMainData:function(){
              let url = 'xxx';
              let state = this.state,
                  keyword = this.searchKey;

              //拼一下当前的hash
              let hash = 'state=' + state;

              if(keyword){
                hash += '&keyword=' + keyword
              }              

              let sendArry = {'state':state,'keyword':keyword}
               this.$http.post(url,sendArry).then(function(response){ 
                if(response.data.status == '2000'){
                    //请求成功后处理
                    //关机监听 修改hash 再打开监听
                    this.listenHash = false;
                    window.location.hash = hash;
                    this.listenHash = true;                           
                }else{
                    this.listenHash = false;
                    window.location.hash = hash;
                    this.listenHash = true;                    
                }
              }, function (response) {
                this.listenHash = false;
                window.location.hash = hash;
                this.listenHash = true;                                 
              }); 
            },
            getUrlHash() {
               let name,value;
               let str=location.href; 
               let num=str.indexOf("#");
               str=str.substr(num+1);
               let arr=str.split("&"); //各个参数放到数组里
               for(let i=0;i < arr.length;i++){
                    num=arr[i].indexOf("=");
                    if(num>0){
                         name=arr[i].substring(0,num);
                         value=arr[i].substr(num+1);

                         //如果遇到数组 JSON.parse(value)
                         //如果遇到数字 parseInt(value)
                         if(name == 'state'){
                          this.state = value;
                         }else if(name == 'keyword'){
                          this.searchKey = value;
                         }else{
                          console.log('else')
                         }
                    }
               }
               this.getMainData();
            },
            listenHashChange(){
                let me = this;
                window.onhashchange = function(){ 
                  if(me.listenHash){
                    me.getUrlHash();
                  }                              
                }
            },
        }

