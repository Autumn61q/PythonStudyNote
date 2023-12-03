第三方包：
![](https://github.com/Autumn61q/PythonStudyNote/commit/22504ff6bdf3b7600c3a6449fca429f364d0b111)

如何安装第三方包：
  用python内置的pip程序即可：
    1.打开命令提示符
    2.输入 pip install 包名称   即可通过网络快速安装第三方包(安装的位置和你输入命令的位置没啥关系）
    ![](https://github.com/Autumn61q/PythonStudyNote/blob/main/imagines/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20231203121443.png)
    删除的话有两种方法
      1）就输入 pip uninstall 包名称  （也不用移动到安装包的目录下）
      2）手动删除包。找到包安装的位置，然后删除（还是算了吧，找不到）
  （附：pip是连接国外的网站，所以有时候很慢，然后下载的时候就可以用如下命令：
       pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称）

第三方包的使用：
  和自己写的包没啥区别。先import一下，然后用
