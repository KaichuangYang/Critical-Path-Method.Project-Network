import project_network_generater
import get_EETs,get_LETs,get_TFs
import numpy as np

def My_CPM(x=[],n=30):
    if x==[] and n !=30:
        print(f'You are running a project network with {n} nodes as you setup')
        G=project_network_generater.project_network_generater(n)
    elif x!=[] and n!=30:
        print('ERRO!Please do not enter x and n simutanously!')
    elif x==[] and n==30:
        print('You are running a project network with 30 nodes as default')
        G=project_network_generater.project_network_generater(n)
    else:
        # if type(x)==list:
        tt=list(map(len,x))
        TT=list(tt[0]*np.ones(len(tt)))
        if TT==tt:
            G=np.array(x)
            print(f'You are running a project network with {tt[0]} nodes as you setup')
        else:
            print('define a n x n matrix with n list, each list has n element, make sure it is a project network maatrix')
        # if type(x)==np.ndarray:
        #     if x.shape[0]==x.shape[1] and len(x.shape)==0:
        #         G=x
        #     else:
        #         print('please enter a n X n 2 dimension matrix!')
    EET=get_EETs.get_EETs(G)
    LET=get_LETs.get_LETs(G,EET)
    TFs_Dict=get_TFs.get_TFs(G,EET,LET)
    critical_Path=[]
    for i in list(TFs_Dict.keys()):
        if TFs_Dict[i]==0:
            critical_Path.append(i)
    count=0
    for i in critical_Path:
        if eval(i)[0]==1:
            count+=1
    #print(count)
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