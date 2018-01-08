title: websoket
date: 2015-10-13 15:57:53
tags: 前端
---
[教程](http://javascript.ruanyifeng.com/htmlapi/websocket.html)见阮一峰的网站
<!--more-->
简述就是安装node.js 
安装express，强烈推荐个[教程](http://cwbuecheler.com/web/tutorials/2013/node-express-mongo/)，可以好好看看
安装soket.io
我直接上代码
index.js

	var app = require('express')();
	var http = require('http').Server(app);
	var io = require('socket.io')(http);
	app.get('/', function(req, res){
		res.sendFile(__dirname + '/index.html');
	});
	io.sockets.on('connection', function (socket) {
	  socket.emit('news', { hello: 'world' });//吐数据
	  socket.on('anotherNews', function (data) {//收数据
	    console.log(data);
	  });
	});
	http.listen(3000, function(){
		console.log('listening on *:3000');
	});

index.html

	<!DOCTYPE html>
	<html>
	    <head>
	        <meta charset="utf-8">
	        <meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=0" name="viewport">
	        <title>websoket</title>
	        <script src="https://cdn.socket.io/socket.io-1.3.7.js"></script>
	    </head>
	    <body>
	        <script>
	            var socket = io.connect('http://localhost:3000');
	            socket.on('news', function (data){
	               console.log(data);
	            }); 
	            socket.emit('anotherNews',{ nice: 'person' });       
	            
	        </script>
	    </body>
	</html>


