# 新概念力学 1-10

import matplotlib.pyplot as plt
from Physics_Model import Project_Motion as pmf
import numpy as np

v_a = 9.8
v_b = 9.8 / np.sqrt(3)
t = 0.5
alpha = 30
beta = 60


res_1 = pmf(v_a, alpha, t)
res_2 = pmf(v_b, beta, t)


# 绘制
plt.plot(res_1[0], res_1[1])
plt.plot(res_2[0]+1.78, res_2[1], c="red")
plt.plot(res_2[0]+2.81, res_2[1], c="green")
plt.title("Correction graph for 1-10", fontsize=24)
plt.show()
