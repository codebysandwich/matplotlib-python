#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : line1.py
# Author            : sanwich <122079260@qq.com>
# Date              : 2021-06-29 10:35:16
# Last Modified Date: 2021-06-30 16:51:28
# Last Modified By  : sanwich <122079260@qq.com>

# import matplotlib.pyplot as plt
# '''
# 输出可用字体
# import matplotlib as mpl
# print(mpl.font_manager.fontManager.ttflist)
# '''
# # 设置支持中文
# plt.rcParams['font.family'] = 'PingFang HK'
# x = ['一季度', '二季度', '三季度', '四季度']
# data = [101, 130, 150, 88]
# fig, ax = plt.subplots()
# ax.plot(x, data)
# plt.show()

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
