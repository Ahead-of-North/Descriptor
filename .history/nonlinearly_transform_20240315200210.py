import numpy as np

'''
0<alpha[i]<1
0<beta[i]<1/pi
'''

def nonlinearly_transform(r,theta,phi,alpha,beta):
    q=[None]*(3 * (len(r)-1) - 2)#len(r)-1是因为r[0]=none,从r[1]开始有物理意义，r1=r[1]
    
    q[1]=np.log(r[1])
    #print(q)    
    q[2]=r[2]**alpha[2]*np.cos(theta[1]+beta[1]*theta[1]*(np.pi-theta[1]))
    #print(q)  
    q[3]=r[2]**alpha[2]*np.sin(theta[1]+beta[1]*theta[1]*(np.pi-theta[1]))
    #print(q)  
    
    for i in range(3,len(r)): 
            if 3*i-5 < len(q):
                q[3*i-5] = r[i]**alpha[i] * np.cos(theta[i-1] + beta[i] * theta[i-1] * (np.pi - theta[i-1]))
                #print(q)  
            if 3*i-4 < len(q):  # To handle the last element when 3*i-4 goes out of the list index
                q[3*i-4] = r[i]**alpha[i] * np.sin(theta[i-1] + beta[i] * theta[i-1] * (np.pi - theta[i-1])) * np.cos(phi[i-2])
                #print(q)  
            if 3*i-3 < len(q):  # To handle the last element when 3*i-3 goes out of the list index
                q[3*i-3] = r[i]**alpha[i] * np.sin(theta[i-1] + beta[i] * theta[i-1] * (np.pi - theta[i-1])) * np.sin(phi[i-2])
                #print(q)  
    return q

r=[0,1,0.2,3,6.5,5]
theta=[0,0.2,3,6.5,100]
phi=[0,0.2,3,3.1,3.14]
alpha=[0.1,0.1,0.1,0.1,0.1,0.1]
beta=[0.1,0.1,0.1,0.1,0.1,0.1]      

q=nonlinearly_transform(r,theta,phi,alpha,beta)
print(q)         


