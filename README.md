# 博客备份
放在BAE上的博客[www.nuomixin.com](www.nuomixin.com)定期备份

一些git备注
同步到github上
git push origin master
同步到bae上 //"bae"命名随意，只是便于记忆了
git remote add bae https://git.duapp.com/appidob6tjdbg35
git push bae master:master
//如果提示需要git pull，则
git pull bae master
//再提交如果还是拒绝，强制提交
git push bae master:master -f

报错
fatal: refusing to merge unrelated histories
git pull origin branchname --allow-unrelated-histories