# A Module for mechanics simulation
# ___________________________________________________#


import matplotlib.pyplot as plt
import numpy as np
from scipy import constants as cons


def Project_Motion(v, theta, time):
    """
    ver.0.2
    Input 3 varible, folat v, float theta, float time.
    v is the initial velocity, theta is the angle, t is the lasting time.
    return a list with two value, the position vector time-sequence on x-axis and on y-axis.
    """


    # A model for Projectile Motion
    # Designed by ABdeeglr on May 22th, 2022.
    # 抛体运动模型, 根据初始速度和方向绘制抛体运动图像.
    # 本函数的主要思路是建立离散时间, 然后通过位置矢量函数绘制图像.


    # Compute Data
    _step = seq[2]/1000
    _theta = seq[1] / 180 * np.pi
    _t = np.arange(0,seq[2],_step)
    v_x = seq[0] * np.cos(_theta) * _t
    v_y = seq[0] * np.sin(_theta) * _t - 1 / 2 * 9.8 * _t * _t
    
    res = [v_x, v_y]
    
    return res
    


