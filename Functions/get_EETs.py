def get_EETs(G):
    '''
    2.1. (Earliest Event time)
    EET is earliset time by which the event associaled with the node can take place. 
    Use the function EET(i) = max{EET(j) + D(a)}  a=(j,i) belongs to backward stars of i . 
    ----------
    input
    G : numpy.ndarry
    -------
    output
    EET : list

    '''
    #Set EET1=0
    EET=[0]
    for i in range(1,G.shape[0]):
        eetL=[]
		# find the node which is connected with node i,then caculate all eet for nodei
        colG=G[:,i]
        for j in range(len(colG)):
            if colG[j] !=-1:
                eet=EET[j]+colG[j]
                eetL.append(eet)
            else:
                continue
        #only append the largest eet as nodei's eet
        EET.append(max(eetL))
    return EET