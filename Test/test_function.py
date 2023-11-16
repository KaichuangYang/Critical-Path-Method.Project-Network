import numpy as np
import pytest
import get_EETs ,get_LETs,get_TFs,My_CPM

G1=np.load('V3_Project_Network_OR2_Assignment/Test/test_data_G1.npy')
G2=np.load('V3_Project_Network_OR2_Assignment/Test/test_data_G2.npy')
EET1=[0, 4, 11, 14]
EET2=[0, 2, 10, 11, 14, 19]
LET1=[0, 4, 13, 14]
LET2=[0, 2, 13, 14, 14, 19]
TF1={'[1, 2]': 0, '[2, 3]': 2, '[2, 4]': 0, '[3, 4]': 2}
TF2={'[1, 2]': 0,'[1, 3]': 3,'[2, 3]': 11,'[2, 5]': 0,'[3, 4]': 3,'[4, 5]': 3,'[4, 6]': 5,'[5, 6]': 0}
CP1=[['path1', [1, 2], [2, 4]]]
CP2=[['path1', [1, 2], [2, 5], [5, 6]]]
 
def test_get_EETs():
    EET11=get_EETs.get_EETs(G1)
    EET22=get_EETs.get_EETs(G2)
    assert EET11==EET1
    assert EET22==EET2

def test_get_LETs():
    LET11=get_LETs.get_LETs(G1,EET1)
    LET22=get_LETs.get_LETs(G2,EET2)
    assert LET11==LET1
    assert LET22==LET2

def test_get_TFs():
    TF11=get_TFs.get_TFs(G1,EET1,LET1)
    TF22=get_TFs.get_TFs(G2,EET2,LET2)
    assert TF11==TF1
    assert TF22==TF2

def test_MyCPM():
    x1=list(map(list,list(G1)))
    x2=list(map(list,list(G2)))
    CP11=My_CPM.My_CPM(x=x1)
    CP22=My_CPM.My_CPM(x=x2)
    assert CP11==CP1
    assert CP22==CP2

if __name__=='__main__':
    pytest.main(["-vs"])
