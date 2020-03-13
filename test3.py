import numpy as ny
x=ny.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y=ny.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])
x1=ny.sum(x)/x.size
y1=ny.sum(y)/y.size
sum1=0
sum2=0
for i in range(x.size):
    sum1=sum1+(x[i]-x1)*(y[i]-y1)
    sum2=sum2+pow((x[i]-x1),2)
w=sum1/sum2
b=y1-w*x1
print("w的值为:%f" %(w))
print("b的值为:%f" %(b))