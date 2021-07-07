---
description: 讲解基本折线图的绘制
---

# 折线图

假设需要绘制一年四个季度的业绩走势图，假设数据为[101, 130, 150, 88]单位为万元。我们绘制如下：
```python
import matplotlib.pyplot as plt
'''
输出可用字体
import matplotlib as mpl
print(mpl.font_manager.fontManager.ttflist)
'''
# 设置支持中文,设置mac下苹方字体
plt.rcParams['font.family'] = 'PingFang HK'
x = ['一季度', '二季度', '三季度', '四季度']
data = [101, 130, 150, 88]
fig, ax = plt.subplots()
ax.plot(x, data)
plt.show()
```
![](https://gitee.com/codebysandwich/source/raw/master/picgo/line1.png)

现在分别绘制两年四个季度的数据并设置绘制的细节：添加图例、设置线型、设置数据点的类型、设置图形大小、设置网格线等。
```python
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'PingFang HK'
x = ['一季度', '二季度', '三季度', '四季度']
data1 = [101, 130, 150, 88]
data2 = [120, 110, 170, 90]
# 设置画布大小
fig, ax = plt.subplots(figsize=(9, 6))
# 绘制图像：c:颜色，ls:线型，marker:数据标记点样式，label:图例标签
ax.plot(x, data1, c='#FF4B00', ls='--', marker='.', label='2020年')
ax.plot(x, data2, c='green', marker='^', label='2021年')
# 设置图像的标题
ax.set_title('季度销售额对比')
# 设置图像y轴标签
ax.set_ylabel('万元')
# 设置y方向网格
ax.grid(axis='y')
# 显示图像的图例标签
ax.legend()
# 调用显示绘制的画布
plt.show()
```
![](https://gitee.com/codebysandwich/source/raw/master/picgo/line2.png)

颜色设置可以使用内置参数`green`，也可以使用16进制`#FF4B00`表示。

## marker样式
| 标记参数 |                                       图例                                       |
|:--------:|:--------------------------------------------------------------------------------:|
|     .    |       ![](https://gitee.com/codebysandwich/source/raw/master/picgo/dot.png)      |
|     o    |     ![](https://gitee.com/codebysandwich/source/raw/master/picgo/circle.png)     |
|     v    |  ![](https://gitee.com/codebysandwich/source/raw/master/picgo/triangle_down.png) |
|     ^    |   ![](https://gitee.com/codebysandwich/source/raw/master/picgo/triangle_up.png)  |
|     <    |  ![](https://gitee.com/codebysandwich/source/raw/master/picgo/triangle_left.png) |
|     >    | ![](https://gitee.com/codebysandwich/source/raw/master/picgo/triangle_right.png) |
|     1    |    ![](https://gitee.com/codebysandwich/source/raw/master/picgo/tri_down.png)    |
|     2    |     ![](https://gitee.com/codebysandwich/source/raw/master/picgo/tri_up.png)     |
|     3    |    ![](https://gitee.com/codebysandwich/source/raw/master/picgo/tri_left.png)    |
|     4    |    ![](https://gitee.com/codebysandwich/source/raw/master/picgo/tri_right.png)   |
|     8    |     ![](https://gitee.com/codebysandwich/source/raw/master/picgo/octagon.png)    |
|     s    |     ![](https://gitee.com/codebysandwich/source/raw/master/picgo/square.png)     |
|     p    |    ![](https://gitee.com/codebysandwich/source/raw/master/picgo/pentagon.png)    |
|     *    |      ![](https://gitee.com/codebysandwich/source/raw/master/picgo/star.png)      |
|     h    |    ![](https://gitee.com/codebysandwich/source/raw/master/picgo/hexagon1.png)    |
|     H    |    ![](https://gitee.com/codebysandwich/source/raw/master/picgo/hexagon2.png)    |
|     +    |      ![](https://gitee.com/codebysandwich/source/raw/master/picgo/plus.png)      |
|     x    |        ![](https://gitee.com/codebysandwich/source/raw/master/picgo/x.png)       |
|     D    |     ![](https://gitee.com/codebysandwich/source/raw/master/picgo/diamond.png)    |
|     d    |  ![](https://gitee.com/codebysandwich/source/raw/master/picgo/thin_diamond.png)  |

为了展示清楚一些,标记用了橙色。这里就不一一展示了，下面列出官网的映射关系：
```
{'.': 'point', ',': 'pixel', 'o': 'circle', 'v': 'triangle_down', '^': 'triangle_up', '<': 'triangle_left', '>': 'triangle_right', 
'1': 'tri_down', '2': 'tri_up', '3': 'tri_left', '4': 'tri_right', '8': 'octagon', 's': 'square', 'p': 'pentagon', '*': 'star',
'h': 'hexagon1', 'H': 'hexagon2', '+': 'plus', 'x': 'x', 'D': 'diamond', 'd': 'thin_diamond', '|': 'vline', '_': 'hline',
'P': 'plus_filled', 'X': 'x_filled', 0: 'tickleft', 1: 'tickright', 2: 'tickup', 3: 'tickdown', 4: 'caretleft', 5: 'caretright',
6: 'caretup', 7: 'caretdown', 8: 'caretleftbase', 9: 'caretrightbase', 10: 'caretupbase', 11: 'caretdownbase', 'None': 'nothing',
None: 'nothing', ' ': 'nothing', '': 'nothing'}
```
