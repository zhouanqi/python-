- 创建仓库 : `mkdir 目录名`、`cd 目录名`

1. 初始化Git仓库 : `git init`
 
1.  添加文件到Git仓库
    
    i. `git add<file>`,可以反复多次使用，添加多个文件
    
    ii.`git commit`
1. 掌握工作区的状态 ： `git status`
1. 查看修改的内容 ：`git diff` 
2. 查看以往修改的内容：`git log`,可以使用参数：`--pretty=onelne`
3. 回退版本：`git reset --hard HEAD^`,上一个版本号用：`HEAD^`,上上一个版本号是：`HEAD^^`，也可以使用版本号回退。
4. 查看命令历史，可方便回退未来的版本：`git relog`
5. 放弃工作区的修改：`git checkout --file`
6. 撤销暂存区修改：`git reset HEAD file(文件名)`
7. 删除：`git rm test.txt`
8. 关联远程的GitHub:`git remote add origin git@github.com:自己的GitHub名/自己的git目录名.git`
9. 推送本地库内容到远程库：`git push -u origin master`
推送时遇到：
```
error: Cannot pull with rebase: You have unstaged changes. 
error: Additionally, your index contains uncommitted changes. 
```
是告诉你有些东西你没有提交，要先提交
解决办法：















