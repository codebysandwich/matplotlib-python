# matplotlib简介

`matplotlib`是建立在`numpy`基础上的多平台可视化程序库。它以多种拷贝格式和跨平台的交互式环境生成出版物质量的图形。

## 安装

在终端中执行以下语句即可完成安装
```shell
pip install matplotlib
```

在python交互环境下执行
```python
>>> import matplotlib as mpl
>>> mpl.__version__
'3.1.2'
```
执行输出的版本号因人而异, 个人建议安装matplotlib之前先安装`numpy`和`pandas`。均可以通过`pip`执行安装。能正常打印出版本号说明安装成功。

## 工具
数据可视化属于数据分析范畴，推荐使用`ipython`环境。工具可以考虑[`jupyter notebook`](https://jupyter.org/)，安装jupyter时会自动安装ipython环境。jupyter安装如下：
```shell
pip install jupyter
```
jupyter可以提供很好的文档查阅功能，以笔记的形式管理好文档和代码。交互式执行程序的方式也比较契合数据分析的特征。

<img src="https://gitee.com/codebysandwich/source/raw/master/picgo/labpreview.png" title="jupyter">

如果需要使用编辑器，也可以使用[`VSCode`](https://code.visualstudio.com/)

<img src="https://gitee.com/codebysandwich/source/raw/master/picgo/vscode.jpg" width="80%" title="vscode">

其他工具例如`PyCharm`、`Vim`等亦可，工具的选取主要还是看个人的使用偏好。

[![](https://gitee.com/codebysandwich/source/raw/master/picgo/pycharm.png)](https://www.jetbrains.com/pycharm/)[![](https://gitee.com/codebysandwich/source/raw/master/picgo/vim.png)](https://neovim.io)

## 第三方包
大量的第三方资源包建立在`matplotlib`的基础上，包括几个高级的绘图包[`seabron`](http://seaborn.pydata.org)、[`ggplot`](https://github.com/yhat/ggpy)以及地图投影绘图包[`basemap`](https://matplotlib.org/basemap/)和[`cartopy`](https://scitools.org.uk/cartopy/docs/latest/)。

## 其他资源
**matplotlib 中文**

[<img src="https://gitee.com/codebysandwich/source/raw/master/picgo/matplotlib_cn_logo.png" width="100px">](https://www.matplotlib.org.cn/)

**matplotlib 官网**

[<img src="https://gitee.com/codebysandwich/source/raw/master/picgo/matplotlib_logo.png" width="40%">](https://matplotlib.org/)

**官方GitHub**

[<img src="https://gitee.com/codebysandwich/source/raw/master/picgo/github_logo.jpg" width="50%">](https://github.com/matplotlib/matplotlib)


