#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : line1.py
# Author            : sanwich <122079260@qq.com>
# Date              : 2021-06-29 10:35:16
# Last Modified Date: 2021-06-29 10:35:16
# Last Modified By  : sanwich <122079260@qq.com>

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
