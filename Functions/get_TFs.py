def get_TFs(G,EET,LET):
    '''
    TF: Total Float
   The float(or slack) of each activity: the amount of time by which each activity can be postponed without affecting the overall duration of the project
    Use the function TF(a)= LET(j)-EET(i)-D(a)    a=(i,j).
    ---------
    input
    LET : list
    EET : list
    G : numpy.ndarry

    ---------
    output
    TFs_Dict : dict
    '''
    n=G.shape[0]
    #find out all node in the project
    nodeList=list(range(1,n+1))
    #using a dict to store all nodes' EET LET
    nodeDict={}
    for i in nodeList:
        nodeDict[i]=[EET[i-1],LET[i-1]]
    conected_nodeList=[]
    # find all activities in the network
    for i in range(G.shape[0]):
        for j in range(i,G.shape[0]):
            if G[i,j]!=-1:
                conected_nodeList.append([i+1,j+1])
    TFs_Dict={}
    #calculate tf of each activity
    for i in conected_nodeList:
        x=i[0]
        y=i[1]
        TFs_Dict[str(i)]=nodeDict[y][1]-nodeDict[x][0]-G[x-1,y-1]
    return TFs_Dict