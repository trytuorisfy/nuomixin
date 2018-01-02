title: datatables笔记
date: 2015-07-12 10:06:44
tags: 前端
---
因为正好用到，自己慢慢摸索了很久，记下写有用的。

第一件事，上官网[datatables](http://datatables.net)。
我发现竟然还有个中文版的，但非官方，授权翻译的，走起[中文版](http://dt.thxopen.com/index.html)
[api集合](https://datatables.net/reference/api/)
[配置选项](https://datatables.net/reference/option/)

<!--more-->

## 修改全局默认配置
    $.extend( true, $.fn.dataTable.defaults, {
        processing: true,
        language: {
            processing:     "数据处理中...",
            search:         "",
            lengthMenu:     "显示 _MENU_ 项结果",
            info:           "显示第 _START_ 至 _END_ 条订单，共 _TOTAL_ 条",
            infoEmpty:      "没有显示条目",
            infoFiltered:   "(由 _MAX_ 项结果过滤)",
            infoPostFix:    "",
            loadingRecords: "数据读取中...",
            zeroRecords:    "无符合数据",
            emptyTable:     "没有数据",
            paginate: {
                first:      "首页",
                previous:   "前一页",
                next:       "后一页",
                last:       "最后"
            },
            aria: {
                sortAscending:  ": 升序排列",
                sortDescending: ": 降序排列"
            }
        },
        responsive: true,
        searching: false,
        ordering: false,
        lengthChange: false
    })

## ajax实用的参数
    var table = $('#table').DataTable({      
            ajax: "url",
            "columns": [
                { "data": "key1" },
                { "data": "key2" }
            ],
            "columnDefs": [
                {
                    "render": function ( data, type, row ) {
                        return row.key + data;//row.key指拿到的json里面的key对应的value，data值对应的"columns"中拿到的第几个值，这里就是第一个值"key1"对应的value
                    },
                    "targets": 0
                },
                {
                    "render": function ( data, type, row ) {
                        return "hello 我是第二个值" + data;
                    },
                    "targets": 1
                }                
            ],
            "drawCallback": function( settings ) { //回调函数
                var api = new $.fn.dataTable.Api( settings );
                var num = api.rows().data().length;   //api.rows().data()就是指拿到的json值
                console.log(num);
            }               
    });


## [重新加载ajax的url](https://datatables.net/reference/api/ajax.url%28%29)
	var table = $('#example').DataTable( {
	    ajax: "data.json"
	} );
	 
	table.ajax.url( 'newData.json' ).load();
## 补充一个重点
关于json格式，最好写成如下方式，取值方便

    {
        "data": { //尽量不要改名 就叫data
            "key1": "value1",
            "key2": "value2"
        }
    }
