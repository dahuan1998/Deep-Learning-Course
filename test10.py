import tensorflow as tf
x=tf.constant([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y=tf.constant([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])
x_aver=tf.reduce_mean(x)#求x平均值
y_aver=tf.reduce_mean(y)#求y平均值

x1=tf.subtract(x,x_aver)#求x与x的平均值差值
y1=tf.subtract(y,y_aver)#求y与y的平均值差值

w1=tf.multiply(x1,y1)#求乘积值
w2=tf.reduce_sum(w1)#求和---分子

w3=tf.subtract(x,x_aver)
w4=tf.pow(w3,2)
w5=tf.reduce_sum(w4)#求和----分母
w=tf.divide(w2,w5)
print("w的值为")
print(w.numpy())

wx_aver=tf.multiply(w,x_aver)
b=tf.subtract(y_aver,wx_aver)
print("b的值为")
print(b.numpy())
