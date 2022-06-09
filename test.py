from sympy import*
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
