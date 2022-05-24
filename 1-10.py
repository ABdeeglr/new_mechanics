# 新概念力学 1-10


import matplotlib.pyplot as plt # 导入图像绘制工具
import numpy as np # 导入向量计算工具
from scipy import constants as cons # 导入数学物理常数



# 基本数据
t = np.arange(0,0.5,0.0001)
pi = cons.pi
alpha = pi / 6
beta = pi / 3
g = 9.8
v_a = 9.8
v_b = 0
ab_1 = 1.78
ab_2 = 2.82901

# 计算
v_b = v_a / np.sqrt(3)
x_a = v_a * np.cos(alpha) * t
y_a = v_a * np.sin(alpha) * t - 1 / 2 * g * t * t

x_b_1 = v_b * np.cos(beta) * t + ab_1
x_b_2 = v_b * np.cos(beta) * t + ab_2
y_b = v_b * np.sin(beta) * t - 1 / 2 * g * t * t



# 绘制
plt.plot(x_a,y_a)
plt.plot(x_b_1,y_b,c="red")
plt.plot(x_b_2,y_b,c="green")
plt.title("Correction graph for 1-10", fontsize=24)
plt.show()
