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
# 设置支持中文
plt.rcParams['font.family'] = 'PingFang HK'
x = ['一季度', '二季度', '三季度', '四季度']
data = [101, 130, 150, 88]
fig, ax = plt.subplots()
ax.plot(x, data)
plt.show()
```
![](https://raw.githubusercontent.com/codebysandwich/sourcerepos/master/pics/line1.png)
