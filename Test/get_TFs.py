def get_TFs(G,EET,LET):
    n=G.shape[0]
    nodeList=list(range(1,n+1))
    nodeDict={}
    for i in nodeList:
        nodeDict[i]=[EET[i-1],LET[i-1]]
    conected_nodeList=[]
    for i in range(G.shape[0]):
        for j in range(i,G.shape[0]):
            if G[i,j]!=-1:
                conected_nodeList.append([i+1,j+1])
    TFs_Dict={}
    for i in conected_nodeList:
        x=i[0]
        y=i[1]
        TFs_Dict[str(i)]=nodeDict[y][1]-nodeDict[x][0]-G[x-1,y-1]
        #print(f'{nodeDict[y][1]}-{nodeDict[x][0]}-{G[x-1,y-1]}')
    return TFs_Dict