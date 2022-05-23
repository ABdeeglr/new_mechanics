# A model for Projectile Motion
# Designed by ABdeeglr on May 22th, 2022.
# 抛体运动模型, 根据初始速度和方向绘制抛体运动图像.
# 本函数的主要思路是建立离散时间, 然后通过位置矢量函数绘制图像.
# ___________________________________________________#


import matplotlib.pyplot as plt
import numpy as np
from scipy import constants as cons


def Project_Motion(seq):
    """
    ver.0.1
    Input varible seq is a list: seq[0] is float v_0, seq[1] is float theta_0, and seq[2] is time t_0
    v_0 is the initial velocity, theta_0 is the angle, t_0 is the lasting time.
    """


    # Collect Data
    _step = seq[2]/1000
    _theta = seq[1] / 180 * np.pi
    _t = np.arange(0,seq[2],_step)
    v_x = seq[0] * np.cos(_theta) * _t
    v_y = seq[0] * np.sin(_theta) * _t - 1 / 2 * 9.8 * _t * _t


    # Yied the Graph
    plt.scatter(v_x,v_y,c=v_x,cmap=plt.cm.Blues,edgecolor='none',s=15)
    plt.show()
    
    return 0
    # 剩下需要修改的地方：
    # 1.多曲线绘图； 2.生成图例太模糊/plot和sca


