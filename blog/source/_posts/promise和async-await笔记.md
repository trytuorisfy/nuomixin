---
title: promise和async/await笔记
date: 2019-07-16 17:51:35
tags: 笔记
---

简单易懂，请看如下：
Promise [大白话讲解Promise（一）吕大豹](https://www.cnblogs.com/lvdabao/p/es6-promise-1.html)
async/await [理解 JavaScript 的 async/await 边城](https://segmentfault.com/a/1190000007535316#articleHeader7)

<!--more-->

笔记来一把：

Promise部分
	
		//定义
		var nowTime = new Promise((resolve,reject) => {
			resolve(new Date())
		})

		//执行
		nowTime.then((data) => {
			console.log(data)
		})

		//捕获错误
		nowTime.then((data) => {
			console.log(data)
		}).catch(function(reason){
	    console.log('rejected');
	    console.log(reason);
		});


async/await部分

		async function testAsync() {
		    return "hello async";
		}

		const result = testAsync();
		console.log(result); //看这里！它已经是个Promise对象了

		//用法
		function takeLongTime(n) {
		    return new Promise(resolve => {
		        setTimeout(() => resolve(n + 200), n);
		    });
		}

		function step1(n) {
		    console.log(`step1 with ${n}`);
		    return takeLongTime(n);
		}

		function step2(n) {
		    console.log(`step2 with ${n}`);
		    return takeLongTime(n);
		}

		function step3(n) {
		    console.log(`step3 with ${n}`);
		    return takeLongTime(n);
		}

		//Promise方法
		function doIt() {
		    console.time("doIt");
		    const time1 = 300;
		    step1(time1)
		        .then(time2 => step2(time2))
		        .then(time3 => step3(time3))
		        .then(result => {
		            console.log(`result is ${result}`);
		            console.timeEnd("doIt");
		        });
		}

		doIt();

		// async/await方法  强势备注：此方法的下面函数可以使用上面函数的结果 即result中可以使用time1 time2 time3
		async function doIt() {
		    console.time("doIt");
		    const time1 = 300;
		    const time2 = await step1(time1);
		    const time3 = await step2(time2);
		    const result = await step3(time3);
		    console.log(`result is ${result}`);
		    console.timeEnd("doIt");
		}

		doIt();





