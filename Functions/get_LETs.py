def get_LETs(G,EET):
    '''
    2.1.(Latest Event Time)
    LET is latest time by which the event associated with the node has to take place for the project duration to be minimized. 
    Use the function LET(i) = min{LET(j) - D(a)}   a=(i,j) belongs to forward stars of i
    ----------
    input
    G : numpy.ndarry
    EET : list
    -------
    output
    LET : list

    '''
	# Set LET(n) = EET(n)
    LET=[EET[-1]]
    for i in range(1,G.shape[0]):
        letL=[]
        # find the node which is connected with node i,then caculate all let for nodei
        rowG=G[G.shape[0]-i-1,:]
        for j in range(len(rowG)):
            if rowG[j] != -1:
                idx=G.shape[0]-j-1
                let=LET[idx]-rowG[j]
                letL.append(let)
            else:
                continue
        #only append the smallest let as nodei's eet
        LET.append(min(letL))
    #make let in right order from let1,let2....letn
    LET.reverse()
    return LET
