#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : lineGen.py
# Author            : sanwich <122079260@qq.com>
# Date              : 2021-07-05 16:16:43
# Last Modified Date: 2021-07-07 13:37:57
# Last Modified By  : sanwich <122079260@qq.com>

import matplotlib.pyplot as plt

if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.plot([1, 3],
            c='#E9E9E9',
            marker='d',
            label='test',
            mec='orange',
            mfc='orange')
    ax.legend()
    plt.show()
