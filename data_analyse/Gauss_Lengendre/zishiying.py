#重复g高斯勒让德法则
import numpy as np
import math
import B
nr1=1
answer1=np.zeros((nr1));err1=np.zeros((nr1));limits1=np.zeros((nr1,2))
answer2=np.zeros((nr1));err2=np.zeros((nr1));limits2=np.zeros((nr1,2))
conv1=np.array([False])
conv2=np.array([False])
#法则2比法则1更准确，nsp2>nsp1
limits1[0,:]=(0.0,1.0);abserr=1e-3;relerr=1e-3;nsp1=1;nsp2=4
samp1=np.zeros((nsp1,1));samp2=np.zeros((nsp2,1));wt1=np.zeros((nsp1));wt2=np.zeros((nsp2))
B.gauss_legendre(samp1,wt1);B.gauss_legendre(samp2,wt2)
print('自适应高斯法则')
print('绝对值错误容差',abserr)
print('相对错误容差',relerr)
print('积分上下限',limits1)
print('低阶高斯勒让德法则',nsp1)
print('高阶高斯勒让德法则',nsp2)
def f63(x):
    f63=x**(1.0/7.0)/(x**2.0+1.0)
    return f63
while(True):
    area=0;tot_err=0;ct=0;cf=0
    for i in range(1,nr1+1):
        if (not conv1[i-1])==True:
            a=limits1[i-1,0];b=limits1[i-1,1]
            nsp1=samp1.shape[0];nsp2=samp2.shape[0]
            wr=b-a;hr=0.5*wr;area1=0;area2=0
            for j in range(1,nsp1+1):
                area1=area1+wt1[j-1]*hr*f63(a+hr*(1.0-samp1[j-1,0]))
            for j in range(1,nsp2+1):
                area2=area2+wt2[j-1]*hr*f63(a+hr*(1.0-samp2[j-1,0]))
            errest=area1-area2;tol=max(abserr,relerr*abs(area2))
            ans=area2;verdict=False
            if abs(errest)<tol:
                verdict=True
            answer1[i-1]=ans;conv1[i-1]=verdict;err1[i-1]=errest
        if bool(conv1[i-1])==True:
            ct=ct+1
        else:
            cf=cf+1
        area=area+answer1[i-1];tot_err=tot_err+err1[i-1]
    if cf==0:
        print('重复数量',nr1)
        print('         小分区上下限         区域面积       误差')
        for i in range(1,nr1+1):
            for j in range(1,3):
                print('{:12.4}'.format(limits1[i-1,j-1]),end='')
            print('{:16.8}'.format(answer1[i-1]),end='')
            print('{:16.8}'.format(err1[i-1]))
        print('解和总误差',area,tot_err)
        break
    limits2[:]=limits1[:];answer2[:]=answer1[:];conv2[:]=conv1[:];err2[:]=err1[:]
    nr2=nr1;nr1=ct+2*cf
    answer1=np.zeros((nr1));conv1=np.zeros((nr1));err1=np.zeros((nr1));limits1=np.zeros((nr1,2))
    conv1[:]=False;inew=0
    for i in range(1,nr2+1):
        if conv2[i-1]==True:
            inew=inew+1
            limits1[inew-1,:]=limits2[i-1,:];answer1[inew-1]=answer2[i-1]
            err1[inew-1]=err2[i-1];conv1[inew-1]=True
        else:
            inew=inew+1;limits1[inew-1,0]=limits2[i-1,0]
            limits1[inew-1,1]=(limits2[i-1,0]+limits2[i-1,1])*0.5
            inew=inew+1
            limits1[inew-1,0]=(limits2[i-1,0]+limits2[i-1,1])*0.5
            limits1[inew-1,1]=limits2[i-1,1]
    answer2=np.zeros((nr1));conv2=np.zeros((nr1));err2=np.zeros((nr1));limits2=np.zeros((nr1,2))
            

