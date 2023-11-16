from Functions import project_network_generater
from Functions import get_EETs,get_LETs,get_TFs
import numpy as np

def My_CPM(x=[],n=30):
    '''

    The function is to compute the EET,LET,TF,critical path of the project network, which means is to sort the critical activites whose TF = 0.
    We call critical any activity with TF=0 and critical path the path they form.

    '''
    #let the user input a matrix by list or the size of a matrix.
    #If the input is the size of a matirx, we will use our project_network_generater function to generate a random matrix.

    # to find what type of input is, test whether the input is valid, if not print the erro type
    if type(x)!=type(np.ones((1,1))):
        if x==[] and n !=30:
            print(f'You are running a project network with {n} nodes as you setup')
            G=project_network_generater.project_network_generater(n)
        elif x!=[] and n!=30:
            print('ERRO!Please do not enter x and n simutanously!')
        elif x==[] and n==30:
            print('You are running a project network with 30 nodes as default')
            G=project_network_generater.project_network_generater(n)
        else:
            tt=list(map(len,x))
            TT=list(tt[0]*np.ones(len(tt)))
            if TT==tt:
                G=np.array(x)
                print(f'You are running a project network with {tt[0]} nodes as you setup')
            else:
                print('define a n x n matrix with n list, each list has n element, make sure it is a project network maatrix')
    # elif type(x)!=type(np.ones((1,1))):
    #     if x.shape[0]==x.shape[1]:
    #         G=x
    #         print('You are running your own project network, please make sure your own matrix is valid for your project network')
    #     else:
    #         print('please input a n x n 2 dim ndarry')
    else:
        print('You are running your own project network, please make sure your own matrix is valid for your project network')
        G=x
    print('The project matrix:')
    print(G)
    EET=get_EETs.get_EETs(G)
    print(f'the EET of the project is{EET}')
    LET=get_LETs.get_LETs(G,EET)
    print(f'the LET of the project is{LET}')
    TFs_Dict=get_TFs.get_TFs(G,EET,LET)
    print(f'the TF of the project is{TFs_Dict}')
    critical_Path=[]
# compute the critical path of the project
    for i in list(TFs_Dict.keys()):
        if TFs_Dict[i]==0:
            critical_Path.append(i)
    count=0
# check the number of critical paths we have for this project
    for i in critical_Path:
        if eval(i)[0]==1:
            count+=1
    #print(count)
# sort all critical paths 
# We denote two connected activities as [a,b][c,d]
# If b=c, then these two activities are in the same critical path
# Otherwise, they are in different critical paths
    CP=[]
    for i in range(count):
        L=['path'+str(i+1)]
        L.append(eval(critical_Path[i]))
        for j in critical_Path:
            if eval(j)[0]==L[-1][-1]:
                L.append(eval(j))
            else:
                continue
        print(f'The NO.{i+1} critical path of this project network is {L}')
        CP.append(L)
    
    return CP