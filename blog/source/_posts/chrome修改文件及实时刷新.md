title: chrome修改文件及实时刷新
date: 2016-02-27 17:23:17
tags: 前端
---

现在有点小激动呢，能直接在chrome中修改文件和看结果啦，完美~
[使用Chrome调试（编辑）JavaScript、CSS、HTML](http://www.poorren.com/chrome-debug-javascript-css-html/)
[实时自动刷新页面来开发](http://cnodejs.org/topic/53427d16dc556e3b3901861e)

整一起步骤如下
下载chrome插件LiveReload
运行如下代码

    npm i livereload -g
到本地的目标文件夹，直接执行

    livereload //成功后提示 safe on port xxxx   不用管这个端口号，因为反正我没用到，还是之前的地址就好

打开chrome的Liveload按钮
以上为告别F5的步骤

在说直接在浏览器中改本地文件的步骤：
在chrome浏览器中，切换到Sources标签(在Console标签右侧)。
在面板左侧，右击后选择"Add folder to workspace"，选中目标文件夹，此时里面的文件就可以编辑了。同时，ctrl+s保存后，编辑后结果也实时保存在了本地文件中，是本地文件！






