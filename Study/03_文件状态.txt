git add readme.txt
git commit -m 'my first commit'

向我们新建的git仓库中添加了对readme.txt文件的版本控制。现在，我们要试图对仓库中的文件进行一些改动，同时观察它们的状态变化，以此实践上节课中说的git工作流。

首先，在命令行的本地仓库工作目录下执行命令：

git status

你会看到：

# On branch master
nothing to commit (working directory clean)

很好，你的目录是干净的，没什么可提交的。说明所有的文件都是未修改的状态，没有未跟踪的文件，也没有修改过未提交的文件。输出的提示还告诉你，目前在branch master上。关于branch的概念我们将在后面的课程中介绍。

接下来，随便用一个文本编辑器去修改一下readme.txt里的文字。另外，再向目录中新建一个test.py文件（也可以从别处copy一个过来）。

再次执行：

git status

得到输出：

# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#	modified:   readme.txt
#
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#	test.py
no changes added to commit (use "git add" and/or "git commit -a")

提示是比较清楚的：readme.txt被修改过了，还有untracked的test.py。提示里也说了，用"git add <file>..."可以添加要提交文件。git add的意思就是，把文件添加到暂存区，也就是我们说的暂存。

那么我们就来用这条命令：

git add readme.txt
git add test.py

然后继续：

git status

再来看结果：

# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#	modified:   readme.txt
#	new file:   test.py
#

"Changes to be committed"里列出的就是已暂存的文件，它们将在commit时被提交。

执行：

git commit -m 'test file status'

将修改和增加的文件提交。-m后面的参数是提交时的注释。输出提示会告诉你这次提交做了哪些改动。

最后再来执行一遍：

git status

可以看到又回到了最初未修改的状态。刚刚做的所有改动都已经被git所记录。

通过命令：

git log

可以查看到之前提交的历史记录。


在前面的过程中，可能会因为你所用编辑器的备份机制，在目录中产生一些奇怪的文件，比如readme.txt~。这类文件也会被列在未跟踪的列表中。下节课我们来说下如何避免这些我们不想关注的文件，以及其他一些在提交过程中的常用到的命令。
