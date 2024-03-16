import numpy as np

# 创建一个矩阵
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# 计算矩阵的秩
rank = np.linalg.matrix_rank(A)
a = int(rank)
print(a)
print(type(a))

print("矩阵的秩是：", rank)