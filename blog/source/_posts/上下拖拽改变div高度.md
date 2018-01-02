title: 上下拖拽改变div高度
date: 2017-10-23 14:29:40
tags: 前端
---

看到grid布局，正好想到用到过上下拖拽横向改变div高度，觉得用这个布局会方便很多，于是来了一把。
实在人直接贴代码。
布局就是顶部一个固定的导航条，底部的div是固定的，有个初始高度。
备注：其中的drag函数的代码是之前网上找的，但不记得出处了，万一作者本人看到的话，请把链接砸给我。

<a href="http://7sbkqu.com1.z0.glb.clouddn.com/drag.html" target="_blank">效果查看</a>

<!--more-->

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>上下拖拽改变div高度</title>
        <style>
            body{
                margin:0;
            }
            .grid-container {
                display: grid;
                grid-template-rows: 40px 1fr 4px 200px;
                position: fixed;
                top: 0;
                right: 0;
                bottom: 0;
                left: 0;            

            }
            .item-1{
                background-color: black;
                color: #fff;
                line-height: 40px;
            }       
            .item-2{
                background-color: pink;
                overflow:auto;
            }
            .item-3{
                background-color: #d6d6d6;
                cursor: n-resize;
            }       
            .item-4{
                background-color: orange;
                overflow: auto;
            }
        </style>
    </head>
    <body>
        <div class="grid-container" id="grid-container">
            <div class="item-1 item">header 高度40</div>
            <div class="item-2 item">
                <p>起始</p>
                <p>自适应内容区</p>
                <p>自适应内容区</p>
                <p>自适应内容区</p>
                <p>自适应内容区</p>
                <p>自适应内容区</p>
                <p>自适应内容区</p>
                <p>自适应内容区</p>
                <p>自适应内容区</p>
                <p>自适应内容区</p>
                <p>自适应内容区</p>
                <p>自适应内容区</p>
                <p>自适应内容区</p>
                <p>自适应内容区</p>
                <p>自适应内容区</p>
                <p>结束</p>

            </div>
            <div class="item-3 item" id='drag-line'></div>
            <div class="item-4 item" id='move-box'>
                <p>起始</p>
                <p>固定在底部的内容区</p>
                <p>固定在底部的内容区</p>
                <p>固定在底部的内容区</p>
                <p>固定在底部的内容区</p>
                <p>固定在底部的内容区</p>
                <p>固定在底部的内容区</p>
                <p>固定在底部的内容区</p>
                <p>固定在底部的内容区</p>
                <p>固定在底部的内容区</p>
                <p>固定在底部的内容区</p>
                <p>结束</p>
            </div>
        </div>
        <script>
            drag();
            function drag(upDivId){
                var obj = document.getElementById('drag-line');
                var oBox = document.getElementById('move-box');
                //当鼠标在当前区域按下时
                obj.onmousedown = function(ev) {
                    //事件捕获
                    var oEvent = ev || event,
                    //存储当前的一些值
                    //当前物体的宽高
                    oPreW = oBox.offsetWidth,
                    oPreH = oBox.offsetHeight,

                    //当前物体离祖先定位左边和顶部的距离
                    oPreL = oBox.offsetLeft,
                    oPreT = oBox.offsetTop,
                    //当前事件点（鼠标）离可视区的距离
                    oPreX = oEvent.clientX,
                    oPreY = oEvent.clientY;

                    var wrapper = document.getElementById('grid-container');

                    //当鼠标移动时
                    document.onmousemove = function(ev) {
                        var oEvent = ev || event;
                        var oChaY = oPreY - oEvent.clientY;
                        var tarHeight = oPreH + oChaY;
                        if(tarHeight <= 40){ //40为底部固定div留出的最小高度
                            return false;
                        }else{
                            wrapper.style.gridTemplateRows = "40px 1fr 4px " + tarHeight + "px"; //如果知道如何修改单个值的话，欢迎留言
                        }
                        
                    };
                    //当鼠标抬起时
                    document.onmouseup = function() {
                        console.log('up')
                        //当之前的鼠标移动和抬起事件失效
                        document.onmousemove = null;
                        document.onmouseup = null;

                    };
                    //阻止默认行为
                    return false;
                };      
            }
        </script>    
    </body>
    </html>