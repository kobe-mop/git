在文件夹中，经常会有些“其他”文件，比如上节课最后提到的，编辑器产生~结尾的备份文件，或者一些临时文件。又可能，某些文件我们只是在本地使用，并不想提交到远程的仓库中被别人看到。但如果我们不跟踪这些文件，Git会一直很执着地提醒我们工作目录中有一些未被跟踪的文件。如果你想清净一点，就可以通过.gitignore文件忽略你不想看到的文件。

要感受一下忽略文件的效果，首先你得有打算忽略的文件，所以我们强行创建一个叫做readme.txt.tmp的文件，假设它是readme.txt产生的临时文件。

git status 看一下效果，同上节课中一样，在untracked files里列出了这个文件：

# On branch master
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#	readme.txt.tmp
nothing added to commit but untracked files present (use "git add" to track)

然后我们在工作目录中新建一个.gitignore文件，在里面写上一行：

*tmp

保存退出，再运行 git status：

# On branch master
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#	.gitignore
nothing added to commit but untracked files present (use "git add" to track)

readme.txt.tmp文件消失了，untracked files里只剩下刚创建的.gitignore文件。

来看一下《Pro Git》里对.gitignore格式规范的解释：

所有空行或者以注释符号 ＃ 开头的行都会被 Git 忽略。
可以使用标准的 glob 模式匹配。
匹配模式最后跟反斜杠（/）说明要忽略的是目录。
要忽略指定模式以外的文件或目录，可以在模式前加上惊叹号（!）取反。

所谓的 glob 模式是指 shell 所使用的简化了的正则表达式：
星号（*）匹配零个或多个任意字符；
[abc] 匹配任何一个列在方括号中的字符（这个例子要么匹配一个 a，要么匹配一个 b，要么匹配一个 c）；
问号（?）只匹配一个任意字符；
如果在方括号中使用短划线分隔两个字符，表示所有在这两个字符范围内的都可以匹配（比如 [0-9] 表示匹配所有 0 到 9 的数字）。

所以我们前面写的 *tmp，就是指忽略所有以tmp结尾的文件。

再来看一个 .gitignore 文件的例子：

# 此为注释 – 将被 Git 忽略
# 忽略所有 .a 结尾的文件
*.a
# 但 lib.a 除外
!lib.a
# 仅仅忽略项目根目录下的 TODO 文件
# 不包括 subdir/TODO
/TODO
# 忽略 build/ 目录下的所有文件
build/
# 忽略 doc 目录下的所有 .txt 文件
# 会忽略 doc/notes.txt 
# 但不包括 doc/server/arch.txt
doc/*.txt

当然，你也可以把.gitignore文件本身从git中忽略。但我不建议这么做，而是所有协作开发者使用统一的规范，避免有人因为没写.gitignore而提交上去一些奇怪的文件。

在项目一开始就把.gitignore设置好，不仅是为了好看，也是避免不必要的文件对代码产生干扰。比如有些需要本地生成的文件，如果放在远程仓库中被其他人下载使用，也可能会导致程序无法正常运行。
