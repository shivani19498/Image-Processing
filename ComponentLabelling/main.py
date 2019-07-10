import numpy as np
import matplotlib.pyplot as plt

a=[[0,1,1,1],[0,0,1,1],[1,0,1,0],[1,1,0,1]]
a=np.array(a)
n=a.shape[0]

plt.imshow(a,cmap = plt.get_cmap('gray'),extent=[0,n,0,n])
plt.xticks(np.arange(0, n+1, 1))
plt.yticks(np.arange(0, n+1, 1))
plt.grid()
plt.show()

for i in range(n):
    for j in range(n):
            f=a.copy()
            f[i][j]=10
            print("4-connected components of (",i,",",j,") are")
            if i-1>=0 and a[i-1][j]==1:
                f[i-1][j]=8
                print("(",i-1,",",j,")")
            if i+1<n and a[i+1][j]==1:
                f[i+1][j]=8
                print("(",i+1,",",j,")")
            if j-1>=0 and a[i][j-1]==1:
                print("(",i,",",j-1,")")
                f[i][j-1]=8
            if j+1<n and a[i][j+1]==1:
                print("(",i,",",j+1,")")
                f[i][j+1]=8
            print(f)
            plt.clf()
            plt.imshow(f,extent=[0,n,0,n])
            plt.xticks(np.arange(0, n+1, 1))
            plt.yticks(np.arange(0, n+1, 1))
            plt.grid()
            plt.show()