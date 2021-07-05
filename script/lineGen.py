#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : lineGen.py
# Author            : sanwich <122079260@qq.com>
# Date              : 2021-07-05 16:16:43
# Last Modified Date: 2021-07-05 16:38:45
# Last Modified By  : sanwich <122079260@qq.com>

import matplotlib.pyplot as plt

if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.plot([1, 3], marker='d', label='test')
    ax.legend()
    plt.show()
