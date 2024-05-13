import numpy as np

def euler_meth1(fld,t0,y0,n,h):
    t = np.zeros(n+1)
    y = np.zeros (n+1)
    t[0]= t0
    y[0]=y0
    for i in range (n):
        t[i+1] = t[i]+h
        y[i+1]= y[i]+h*fld(t[i],y[i])
    return t,y
def euler_meth(fld,fld1,t0,y0,y10,n,h):
    t = np.zeros(n+1)
    y1 = np.zeros (n+1)
    y2 = np.zeros(n+1)
    t[0]= t0
    y1[0]=y0
    y2[0]=y10
    for i in range (n):
        y1[i+1]= y1[i]+h*float(fld(t[i],y1[i],y2[i]))
        y2[i+1]= y2[i]+h*float(fld1(t[i],y1[i],y2[i]))
        t[i+1] = t[i]+h
    return t,y1,y2

def euler_Mejorado_meth(fld,t0,y0,n,h):
    t=np.zeros(n+1)
    y = np.zeros (n+1)
    y_ = np.zeros(n+1)
    t[0]= t0
    y[0]=y0
    y_[0] = y0
    for i in range (n):
        t[i+1] = t[i]+h
        y_[i+1] = y[i]+h*fld(t[i],y[i])
        y[i+1]= y[i]+h*(fld(t[i],y[i])/2+fld(t[i+1],y_[i+1])/2)
    return t,y
def euler_Mejorado_meth1(fld,t0,y0,n,h):
    t=np.zeros(n+1)
    t_=np.zeros(n+1)
    y = np.zeros (n+1)
    y_ = np.zeros(n+1)
    t[0]= t0
    t_[0]=t0+(h/2)
    y[0]=y0
    y_[0] = y0+fld(t0,y0)*(h/2)
    for i in range (n):
        t_[i+1] = t_[i]+h
        t[i+1] = t[i]+h
        y_[i+1] = y[i]+(h/2)*fld(t[i],y[i])
        y[i+1]= y[i]+h*fld(t_[i+1],y_[i+1])
    return t,y

