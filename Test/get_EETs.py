def get_EETs(G):
    EET=[0]
    for i in range(1,G.shape[0]):
        eetL=[]
        colG=G[:,i]
        for j in range(len(colG)):
            if colG[j] !=-1:
                eet=EET[j]+colG[j]
                eetL.append(eet)
            else:
                continue
        EET.append(max(eetL))
    return EET