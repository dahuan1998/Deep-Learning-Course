import matplotlib.pyplot as plt
import numpy as ny
import tensorflow as tf

boston_housing = tf.keras.datasets.boston_housing
(train_x,train_y),(_,_)=boston_housing.load_data(test_split=0)

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

titles=["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAO","TAX","PTRATIO","B-1000","LSTAT","MEDV"]


plt.figure(figsize=(13,13))
for i in range(13):
    plt.subplot(4,4,(i+1))
    plt.scatter(train_x[:,i],train_y)
    plt.xlabel(titles[i])
    plt.ylabel("Price($1000's)")
    plt.title(str(i+1)+"."+titles[i]+"-Price")
plt.tight_layout(rect=[0,0,1,0.9])
plt.suptitle("各个属性与房价得关系")
plt.show()