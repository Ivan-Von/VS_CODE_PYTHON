import numpy as np
from sympy import *
import sympy
import math
import matplotlib.pyplot as plt
from sympy.simplify.fu import L


class Newton_Co:
    def __init__(self,Small,Big,x,drive):
        self.Small = Small 
        self.Big = Big
        self.x = x
        self.drive = drive
        
    def function(self,x):
        # 得到数学函数
        return (x*sympy.exp(x))/((1+x) ** 2)
    
    def calu_xishu(self,index,number,array):
        # 判断(-1)^n-k
        if (index - number)%2 ==0:
            res = 1
        else:
            res = -1
            # 算柯特斯系数被积函数中的(t-j)多项式
        for i in range(index+1):
            if i!=number:
                res  =res*(self.x-i)
        # 采用sympy库来计算积分
        result = integrate(res,(self.x,0,index))
        # n! 和(n-k)!
        n_fac = self.jieCheng(number)
        n_k_fac = self.jieCheng(index-number)
        result = result/(index*n_fac*n_k_fac)
        array[index-1][number] = result
        print(f"{result}",end = '\t')
    # 算n!
    def jieCheng(self,val):
        res = 1
        while val>=1:
            res = res*val
            val-=1
        return res
    
    def calu_Cotes(self):
        # 保存柯特斯系数，只算到n=8时，后面出现负值，一般不用
        array = np.zeros((self.drive,self.drive+1),dtype = float)
        for i in range(self.drive):
            for j in range(i+2):
                self.calu_xishu(i+1,j,array)
            print()
        # 最后的积分值
        result = self.calu_final(array)
        return result
    
    def calu_final(self,array):
        
        Jianju = (self.Big-self.Small)/self.drive
        result = 0
        for j in range(self.drive+1):
            # 算每一个的积分值，array里面为牛顿科特斯系数
            result += array[self.drive-1][j]*(self.function(self.Small+(Jianju*j)))
        # 乘于（b-a)
        result *=(self.Big-self.Small)
        return result
    
    def calu_trueValue(self):
        res = integrate((self.x*sympy.exp(self.x))/((1+self.x) ** 2),(self.x,self.Small,self.Big))
        return res
        
    def draw(self):
            # 画图
            x_n = np.linspace(Small, Big, 100)
            y_n = []
            for j in range(len(x_n)):
                res = self.function(x_n[j])
                y_n.append(res)

            l2 = plt.plot(x_n, y_n, linestyle='--')
            plt.xlabel('x', fontsize=10, color='k')  # x轴label的文本和字体大小
            plt.ylabel('y', fontsize=10, color='k')  # y轴label的文本和字体大小
            plt.xticks(fontsize=14)  # x轴刻度的字体大小（文本包含在pd_data中了）
            plt.yticks(fontsize=14)  # y轴刻度的字体大小（文本包含在pd_data中了）
            plt.title('y = (x*exp(x))/((1+x)^2)', fontsize=28)  # 图片标题文本和字体大小
            plt.show()

if __name__ == '__main__':
    # 指定定义域
    x = symbols('x')
    print("下面是牛顿科特斯求积算法")
    print("输入积分上界")
    Big = float(input())
    print("输入积分下界")
    Small = float(input())
    print("输入想划分的等份")
    drive = int(input())
    # accurancy =float(input())
    newton = Newton_Co(Small,Big,x,drive)
    integration= newton.calu_Cotes()
    true_value = newton.calu_trueValue()
    print(f"最后的计算结果:{integration}")
    print(f"真实值：{true_value}")
    print("误差：{}".format(math.fabs(true_value - integration)))
    newton.draw()