#Author: Kaichuang Yang    Email:ky1u22@soton.ac.uk
#Before you run this document, make sure you have install the requirements.txt
#run 'pip install -r requirments.txt' for windows and Linux in terminal
#run 'pip3 install -r requirments.txt' for Mac in terminal
from Functions import My_CPM
import numpy as np

print('='*50+'WELCOME!'+'='*50)
print('This is MATH2013 Operational Research II 2022_23 Project Network Assignment')
print('')
print('Author: Kaichuang Yang    Student ID:34347291   Email:ky1u22@soton.ac.uk')
print('')
print("* By running this program, you will get your network's properties, including EET, LET, ET, and Critical Path")
print('')
print('* If you already have a network matrix, you can input a matrix or a list')
print('')
print("* If you do not have one, don't worry, just input a natrual number,we will generate a random project for you")
print('='*50+'START!!!'+'='*50)
x1=input('Please input 0,if you do not have your own project,else,input 1:')
if x1=='0':
    y1=input("please enter the project neteork's node number:")
    My_CPM.My_CPM(n=eval(y1))
elif x1=='1':
    print('please enter your matrix by path or list')
    x2=input('by path enter 1,by list enter 2:')
    if x2=='1':
        y2=input("please enter your matrix document's path,must be a .npy document:")
        y22=np.load(y2)
        My_CPM.My_CPM(x=y22)
    elif x2=='2':
        y3=input('please enter your list:')
        y33=eval(y3)
        My_CPM.My_CPM(x=y33)
print('')
print('* There is a Pytest framwork to test get_EETs,get_LETs,get_TFs,and My_CPM, they are tested through the two networks in lecture notes')
print('* Run test_functiom.py to start test')
print('* All functions under the Function folder are with comments')
print('* The solution to 2.4 is project_network_generater.py')
print('='*50+'**END!**'+'='*50)




