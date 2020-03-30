import tensorflow as tf
import numpy as np
x1 = np.array([137.97, 104.50, 100.00, 124.32, 79.20, 99.00, 124.00,
               114.00, 106.69, 138.05, 53.75, 46.91, 68.00, 63.02, 81.26, 86.21])
x2 = np.array([3, 2, 2, 3, 1, 2, 3, 2, 2, 3, 1, 1, 1, 1, 2, 2])
y = np.array([145.00, 110.00, 93.00, 116.00, 65.32, 104.00, 118.00,
              91.00, 62.00, 133.00, 51.00, 45.00, 78.50, 69.65, 75.69, 95.30])

x0 = np.ones(len(x1))
X = np.stack((x0, x1, x2), axis=1)
Y = y.reshape(-1, 1)

Xt = tf.transpose(X)
XtX_1 = tf.linalg.inv(tf.matmul(Xt, X))
XtX_1Xt = tf.matmul(XtX_1, Xt)
W = tf.matmul(XtX_1Xt, Y)
W = tf.reshape(W, [len(W), 1])
# Sprint(W)
xs = float(input("请输入商品房面积:"))
if xs < 20 or xs > 500:
    xs = float(input("输入不合法，请重新输入："))
xl = int(input("请输入房间数:"))
if xl < 1 or xl > 10:
    xl = int(input("输入不合法，请重新输入："))
Y = 11.96729093+0.53488599*xs+14.33150378*xl

print("预测房价为：%f" % (Y))
