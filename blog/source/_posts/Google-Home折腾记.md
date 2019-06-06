---
title: Google Home折腾记
date: 2019-01-23 14:50:01
tags: 亲测
---

简单备忘：
1.vps走起
	登陆vps装上ss，我的是CentOS7.5，安装如下：

	wget --no-check-certificate -O shadowsocks-libev.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks-libev.sh
	chmod +x shadowsocks-libev.sh
	./shadowsocks-libev.sh 2>&1 | tee shadowsocks-libev.log

2.路由器走起
	本来用的是小米的mini，但总觉得速度跑不起来，最后换了小米的3g，一路艰辛省略，直接上能用的结果，来源为[Monlor-Tools](https://github.com/monlor/Monlor-Tools)。
	具体设置看此工具的github教程，我选的是科学上网方式:全局，然后再将google home的上网方式设置为科学上网，其他设备正常上网。
	一键安装如下：

		sh -c "$(curl -kfsSl https://coding.net/u/monlor/p/Monlor-Tools/git/raw/master/install.sh)" && source /etc/profile &> /dev/null

收工，叫一声 "ok,google"，就有彩色的顶灯亮起，可以调戏咯。

<!--more-->


以下闲聊，音乐用的是spotify播，本来随便收藏了2首韩文歌，结果天天给我播韩文歌，后来，把自己网易云和虾米的歌单导入了进去，结果终于在昨天听上了中文歌...
关于导入，这里也记录下，实用。
在[spotlistr](https://www.spotlistr.com/search/textbox)的输入框里填入“歌名-歌手” ,一行一条。
现在的问题就是怎么把歌单导出成这样的形式。
网易云音乐：
看[这里](https://www.zhihu.com/question/31816805/answer/347366850)，油猴+插件。
[火狐油猴](https://addons.mozilla.org/zh-CN/firefox/addon/tampermonkey/?src=search) [chrome油猴](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=zh-CN) [插件](https://greasyfork.org/zh-CN/scripts/39807-%E5%AF%BC%E5%87%BA%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90%E6%AD%8C%E5%8D%95)
再贴一个python的版本，但我没试，先存着吧[python代码](https://blog.csdn.net/VoidK2/article/details/77508453)
虾米：
看[这里](https://github.com/zhang435/Music-Porter) 但虾米导入到一定程度会报错，所以至今我的歌单没导全...

再补一个关于vps的坑，想换一个配置，然后新开了个配置，愣是连不上ssh。到最后我终于知道了为什么ping的通，ssh就是连不上，端口关闭，我怎么知道的呢，中间心酸省略，结论就是要满足这以下条件，你的vps才算稳了。
1. ping的通
2. 22端口打开 [测试网站](http://coolaf.com/tool/port)




	