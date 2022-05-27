import numpy as np

def normx(x,norm):
    #求一个向量的范数，目前只支持无穷范数。
    if(norm=="inf"):
        #相当于先取绝对值了。
        x=np.maximum(x,-x)
        return np.max(x)

def sor(A,b,w,x0,limit):
    index = 0
    n=A.shape[1]
    D=np.zeros((n,n))
    for i in range(n):
        D[i][i]=A[i][i]
    L=np.zeros((n,n))
    for i in range(n):
        for j in range(i):
            L[i][j]=-A[i][j]
            
    U=np.zeros((n,n))
    for i in range(n):
        for j in range(i+1,n):
            U[i][j]=-A[i][j]
    BS=np.linalg.inv(D-w*L)
    f=np.matmul(BS,w*b)
    BS=np.matmul(BS,(1-w)*D+w*U)
    x=np.matmul(BS,x0)+f
    while(normx(x-x0,"inf")>limit):
        index += 1
        x0=x
        x=np.matmul(BS,x0)+f
    print("最终结果",x)
    print("迭代次数",index)
    return x   




A=np.array([[4,-1,0],[-1,4,-1],[0,-1,4]])
b=np.array([1,4,-3])
x0=np.array([0,0,0])
limit=0.000005
print("A为",A)
print("b为",b)
print("limit为",limit)
w = 1.03
print("w为",w)
sor(A,b,w,x0,limit)
w = 1
print("w为",w)
sor(A,b,w,x0,limit)
w = 1.1
print("w为",w)
sor(A,b,w,x0,limit)