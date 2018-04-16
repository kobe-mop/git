有进就有出，有借就得有还。有添加文件，自然也必须得有移除文件。当不想继续对某个文件进行版本控制的时候，就需要把它从 Git 中移除。

从 Git 中移除一个文件，本质上做的事情就是把这个文件从暂存区中删除，然后提交。完成这个任务要用到命令 git rm。

为了演示删除，我们先向工作目录中添加一个待删除的文件 to_be_deleted.txt，然后 git add，git commit 把它提交到仓库中。

然后我们再将它从目录中删除。

运行 git status 看下状态：

# On branch master
# Changes not staged for commit:
#   (use "git add/rm <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#	deleted:    to_be_deleted.txt
#
no changes added to commit (use "git add" and/or "git commit -a")

Git发现了一处文件改动：有个文件被删掉了。但这仅仅是从你的工作目录中删除了文件，而 Git 仍然在跟踪这个文件，并将会一直提示这个文件的删除状态。

同 git add 添加文件至暂存区类似，用 git rm 命令把文件从暂存区中删除：

git rm to_be_deleted.txt
git status

# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#	deleted:    to_be_deleted.txt
#

删除 to_be_deleted.txt 文件的操作已经被记录在了暂存区，换句话说就是，这个文件被从暂存区删除。接下来：

git commit -m 'remove file'

这样一来，这个曾经被跟踪的文件就从 Git 中移除了，以后的版本就没它什么事了。

那么如果我们是手滑误删了文件呢？没关系，这也是我们使用版本控制的重要原因之一——恢复文件。下节课来讲。
