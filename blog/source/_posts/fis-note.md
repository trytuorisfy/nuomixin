title: F.I.S 笔记(百度的前端工具框架)
date: 2014-12-05 11:28:37
tags: 前端
---
虽然还没真的用到实际项目上，但我觉得这个是大大的好！
被同事打趣为鱼的记性的我，还是把过程给简单记一下。
上官网[F.I.S官网](http://fis.baidu.com/index.html)
<!--more-->

## 安装
安装环境: node.js、npm
备注：命令输入方法  在文件夹空白处右击，选择“Git Bash Here”

    npm install -g fis
## 使用
- 进入项目目录
-  启动服务器(fis 自带了)
       fis server start
- 编译并发布项目
       fis release 
     词条命令的参数说明,直接上图
![fis release 命令参数](http://tuorisfy.qiniudn.com/jianshu/images/fisrelease.jpg)
挑我用过的说下：

	  -d 指定编译完成后的项目输出文件夹
	  -m 为文件增加md5戳
	  -o 压缩文件
	  -p 打包文件，就是把指定的文件合成一个文件
	  -D 指定服务器名（这个有用 我当时在配置文件中配置好后，愣是没输这个命令，然后就是不对，我这智商）
	  -w 监听文件变化(就是不用每次改个东西 再编译一次 刷新下就好了)
  	-L 有修改时自动刷新服务器

我的总结如下：
进入项目文件夹后，
项目开始时：

      fis server start //启动服务器
项目进行中：


    fis release -wL //修改文件 看实时效果
项目完成要输出到文件夹时：

    fis release -omp -D -d ./output  //给项目压缩打包输出到指定文件夹
    //-D不配置的话 默认是根目录 -d 后面跟的 ./output 就是自定义的输出目录 大家随意
项目结束：

    fis server clean //清理掉缓存
    fis server stop //关闭服务器

## 配置
直接扔个配置文件上来，因为我也不大会弄，深奥的就请大家看文档了。



    //配置文件：fis-conf.js
    //打包配置 指定文件夹中的js都会被合并到  pkg文件夹下的lib.js文件中
	fis.config.set('pack', {
		'pkg/lib.js': [
			'/lib/mod.js',
			'/modules/underscore/**.js',
			'/modules/backbone/**.js',
			'/modules/jquery/**.js',
			'/modules/vendor/**.js',
			'/modules/common/**.js'
		]
	});
    //指定服务器 以下示例为将所有css文件http://localhost:8080
    fis.config.merge({
        roadmap : {
            domain : {
                //所有css文件添加http://localhost:8080作为域名
                '**.css' : 'http://localhost:8080'
            }
        }
    });
    //以上配置生效的命令为  fis release -p -D

收工！








