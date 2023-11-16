from random import randint,random
import numpy as np

def project_network_generater(n=30):
    '''
    2.4.
    The function is to generate a n*n type matrix G describing a  random project network.
    g(i,j) is the ijth element of G which means the activity duration from node i to node j.
    Notice that, when the value of the g(i,j) is -1, there is no activity between i and j.
    The matrix conforms the following constraints:
    1.The bottom left of the matrix is -1 because this is a single-direction graph
    2.There is always a path of '1->2->3->...->n', so g(i,i+1) can't be -1.
    3.And each column of the matrix has at most 4 positive integer elements, which means the maximum in-degree for a node is 4.
    
    -------
    input
    n : int.
    ---------
    output
    G:numpy.ndarray.

    '''

    G=np.ones((n,n))  
# To implement the constraint 1                     
    G*=-1                                 
# generate the elements in G randomly
# using a uniform(0,1) to simulate wether the two node should be connected with probability=0.5
    for i in range(n):                    
            for j in range(i+1,n):
                connect_index=random() 
                if connect_index<0.5:
                    G[i,j]=randint(-1,10)
                else:
                    G[i,j]=-1
# This loop is to implement the constraint 2 
    for i in range(n-1):
        j=i+1
        G[i,j]=randint(0,10)
# This loop is to implement the constraint 3
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