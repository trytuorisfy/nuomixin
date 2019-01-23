title: typecho相关（地址重写，七牛）
date: 2015-06-18 15:08:02
tags: 亲测
---
亲测通过，过程如下：
## 地址重写
1. 进入vpsmate
2. 进入网站管理
3. 在对应的域名的设置里面打开rewrite，内容则填写如下
    rewrite (.*) /index.php;
4. 重启nginx后，在typecho后台的永久链接中就可以启用咯

## 七牛云存储
引用下教程，看这里：
[ABEL的博客](http://www.abelyao.com/typecho-qiniufile/)
### 图片上传时保持原名
因为插件默认会重新修改图片的名称，所以我进去小改了下，同时用了七牛的图片处理api，让图片宽度保持在500px。
修改的地方就2处：

    //第一处
    //修改前
    $savename = $savepath . sprintf('%u', crc32(uniqid())) . '.' . $ext;
    //修改后
    $savename = $savepath . $file['name'];

    //第二处
    //修改前
    'path'  =>  $savename,
    //修改后
    'path'  =>  $savename.'?imageView2/2/w/500',

最后，再附上七牛的[图片处理api](http://developer.qiniu.com/docs/v6/api/reference/fop/image/imageview2.html)，可以自己看着改哈

<!--more-->

## 插入mp3
用的插件是 Dewplayer，我是从[appstore](https://github.com/chekun/AppStore)这个项目中下载的
使用简单，直接如下：

    <mp3>歌曲地址</mp3>

来，放一个我现在的铃声，伦桑 入阵曲

<mp3>http://images.nuomixin.com/music-ruzhenqu-lun.mp3</mp3>

***
## 部署到BAE
好吧，我又在BAE上捣腾了一遍，重点是：
`工具要用vpn！！！`，如果用git的时候，有个配置文件config.inc.php是不认的！
其他的照官方教程来就行了，[点这里](http://docs.typecho.org/bae-install)
