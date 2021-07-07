---
description: 快速了解matplotlib的使用
---

# What's matplotlib

## 简单示例

Matplotlib 在图形（即窗口、Jupyter 小部件等）上绘制数据，最简单的绘制方式如下:
```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()
```
![](https://gitee.com/codebysandwich/source/raw/master/picgo/line_demo.png)

`matplotlib.pyplot`为matplotlib的绘图接口，常用`plt`简写，本书所有部分均用此导入方式！`plt.show()`为显示调取绘图的结果。

这样的方式固然简洁，但是个人更建议使用以下的方式创建绘图:
```python
fig, ax = plt.subplots() # 创建图像与绘图区域(轴:Axes)
plt.plot([1, 2, 3, 4], [1, 4, 2, 3]) # 在轴(绘图区域)上绘制数据
plt.show()
```
我们会得到与上图一致的结果，但是这样的做法的好处在于我们可以将图像与绘图区域分离，并可以独立设置各自的属性。具体细节后面会有说明。
这样我们就使用matplotlib实现了简单的图像绘制。

