1.关于json（JavaScript Object Notation，即 JavaScript对象标记法）

  推荐这篇文章：https://blog.csdn.net/qq_41684621/article/details/113851644
  JSON是一种轻量级的数据交互格式。可以按照JSON指定的格式去组织和封装数据
  JSON本质上是一个带有特定格式的字符串

  功能：
    json就是一种在各编程语言中流通的数据格式，负责不同编程语言的数据传递和交互。

  json格式数据化：
    json和Python格式是无缝衔接的，json其实就是一个长成Python字典或者是嵌套着字典的列表的字符串

  Python和JSON数据的相互转化：
    1.导入json模块
        import json
    2.准备符合json格式要求的Python数据
        data=[{"name":"Qiuiue","age":19}]
    3.将python数据转化为json（如果数据里面有中文的话就在dumps里面再传一个ensure_ascii=False的参数）
        data=json.dumps(data)
    4.将json数据转化为python（就是那个数据要是长成字典那样就转为字典，长成列表也同理）
        data=json.loads(data)

2.pyecharts模块：
  pyecharts是一个由百度开源的数据可视化。凭借良好的交互性，精巧的图标设计，得到了众多开发者的认可。
  Python是富有表达力的语言，很适合用于数据处理。
  当数据分析遇上数据可视化时pyecharts就诞生了。

  相关下载：在终端输入 pip install pyecharts

  相关配置：
    1.分为全局配置和系列配置
      关于全局配置：
        就是说标题、图例、工具箱配置那些东西。因为它们不管是对于哪一种统计图都存在
          set_global_opts方法（这个自己了解吧，太多了,随便粘点码，到时候找到好文再附上）
            from pyecharts.options import (TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts)
            line.set_global_opts(
            title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="50%"),
            legend_opts=LegendOpts(is_show=True),
            toolbox_opts=ToolboxOpts(is_show=True),
            visualmap_opts=VisualMapOpts(is_show=True)
        )

3.搞折线图
  1.导包，导入Line功能构建折线图对象
    from pyecharts.charts import Line
  2.创建一个折线图对象
    line=Line()
  3.给折线图对象添加x轴数据和Y轴数据
    # 在使用add_xaxis和add_yaxis时，应该直接传入列表（下面代码是正确的），而不是将列表放在另一个列表中
    # add_xaxis直接传入包含国家名称的列表，add_yaxis直接传入包含GDP数据的列表，并且指定了系列名称为"GDP"
    line.add_xaxis(["中国","英国","美国"])
    line.add_yaxis("GDP",[30,10,20])
  4.用render方法，将代码生成图像
    line.render()# 注意在所有操作安排完了之后再写这一行
  5.执行这个代码。生成一个.html文件，是一个网页文件
    在vscode里面打开这个网页文件的话，看这个文章：https://blog.csdn.net/qq_41645482/article/details/105006074

4.数据处理
  可以用ab173.com（AB173.com是一个提供各种工具的网站，包括JSON在线编辑器、JSON着色工具等。该网站还提供广告位招租服务。）
