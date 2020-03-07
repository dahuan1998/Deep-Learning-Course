import math
a = int(input("请输入a的值："))
b = int(input("请输入b的值："))
c = int(input("请输入c的值："))
d = pow(b,2)-4*a*c
if d<0:
    print("该一元二次方程无解")
elif d==0:
    x=(-b+math.sqrt(d))/2*a
    print("该一元二次方程有一个解:%d" %(x))
else :   
    x=(-b+math.sqrt(d))/2*a
    y=(-b-math.sqrt(d))/2*a
    print("该一元二次方程有两个解:%d %d" %(x,y))
    