# README
Author ：Linda

Ver 2.0

license ： MIT

------
## 0x00 环境

ver1.0 编写自 python 2.7 ， ver2.0 迁移至python3.6，另外还需要有pip……

> requirment.txt:
> matplotlib==3.1.2
> numpy==1.17.4
> Pillow==6.2.1
> pylab==0.0.2
> reportlab==3.5.32
> simplejson==3.17.0



## 0x01 功能

初始化单词本/单词测试/单词记背情况统计/生成抄写文档/自动更换壁纸

## 0x02 使用

1. 自GitHub下载压缩包并解压到任意目录
2. 在./目录命令行（cmd，powershell）以下命令：
> pip install requirment.txt

如果没换过源，导致下载太慢，可以用下面这行使用临时源：

> pip install requirment.txt -i https://pypi.douban.com/simple

3. 在文件$article.txt$中保存文章/台词的纯文本

4. 命令行：
> python ./article2word.py

article2word.py 会把article.txt中的文章提取单词，保存在word.txt中，实际使用中，可以不执行步骤3-4，直接把单词扔进word.txt，自行选择。

5. 命令行：

> python ./transcrible.py

6. 运行正常的话会出现提示选项，包括$init$、$test$、$status$、$draw$、$change\_wallpaper$五个功能，以下分别介绍各个功能及实现。

7. 如 0x01 。

   init：初始化，调用./dic/stardict.py 访问./dic/ecdict.csv 以初始化单词本，存储包括单词、英译、中译等项 ；

   test：会要求输入一个复习比例，通过用户键入的0或者1来判断会与不会，从而更改是否会在手写复习以及壁纸复习中显示；

   status：统计，会显示未见过的单词、不会单词数、已会单词数、学习中单词数；

   draw：询问并创建所要求页数的pdf，存放至./papers

   change\_wallpaper：生成单词图片，调用FWRW.exe更改桌面，同时存放图片至./imgs

## 0x03 <u>demo</u>nstration

## 0x04 Q&A

新功能/特性推荐，报告bug请提交issues，或联系：i@lixinda.me

还没有Question……

## 0x05 版本更新&bug&TODO

ver 2.0：我才新来的呢，什么版本更新？

bug？什么bug，都是特性！

TODO：

- demo图片的添加
- 使用pyinstaller打包成exe，不需要python环境的可执行文件
- 增量式单词本
- 闭环菜单
