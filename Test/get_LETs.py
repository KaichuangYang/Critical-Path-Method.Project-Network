def get_LETs(G,EET):
    LET=[EET[-1]]
    for i in range(1,G.shape[0]):
        letL=[]
        rowG=G[G.shape[0]-i-1,:]
        for j in range(len(rowG)):
            if rowG[j] != -1:
                idx=G.shape[0]-j-1
                let=LET[idx]-rowG[j]
                letL.append(let)
            else:
                continue
        LET.append(min(letL))
    LET.reverse()
    return LET
