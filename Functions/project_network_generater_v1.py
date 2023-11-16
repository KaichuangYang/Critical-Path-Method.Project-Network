from random import randint
import numpy as np

def project_network_generater(n=30):
    G=np.random.randint(-1,10,size=(n,n))
    # The g(i,j)=-1 ,s.t. i>=j
    for i in range(0 ,n):
        for j in range(i ,n): 
            G[j,i] = -1 
# Make sure node 1 :node n has a full connected path
    for i in range(n-1):
        j=i+1
        G[i,j]=randint(0,10)
# Ensuring at most 4 income
    for i in range(5,n):
        popout_List=[]
        while len(popout_List)<i-4:
            random_Popout_Index=randint(0,i-2)
            if  random_Popout_Index in popout_List:
                continue
            else:
                popout_List.append(random_Popout_Index)
        for item in popout_List:
            G[item,i]=-1
    return G