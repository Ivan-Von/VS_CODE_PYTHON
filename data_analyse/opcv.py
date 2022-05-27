import cv

def FFT(image,flag = 0):
    w = image.width
    h = image.height
    iTmp = cv.CreateImage((w,h),cv.IPL_DEPTH_32F,1)
    cv.Convert(image,iTmp)
    iMat = cv.CreateMat(h,w,cv.CV_32FC2)
    mFFT = cv.CreateMat(h,w,cv.CV_32FC2)
    for i in range(h):
        for j in range(w):
            if flag == 0:
                num = -1 if (i+j)%2 == 1 else 1
            else:
                num = 1
            iMat[i,j] = (iTmp[i,j]*num,0)
    cv.DFT(iMat,mFFT,cv.CV_DXT_FORWARD)
    return mFFT

def FImage(mat):
    w = mat.cols
    h = mat.rows
    size = (w,h)
    iAdd = cv.CreateImage(size,cv.IPL_DEPTH_8U,1)
    for i in range(h):
        for j in range(w):
            iAdd[i,j] = mat[i,j][1]/h + mat[i,j][0]/h
    return iAdd

image = cv.LoadImage('F\\Matlab\\circle.jpg',0)
mAfterFFT = FFT(image)
mBeginFFT = FFT(image,1)
iAfter = FImage(mAfterFFT)
iBegin = FImage(mBeginFFT)

cv.ShowImage('image',image)
cv.ShowImage('iAfter',iAfter)
cv.ShowImage('iBegin',iBegin)

cv.WaitKey(0)