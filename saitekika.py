import numpy as np
from copy import copy
import math

question_num = input("Please input question number:")
method_num = input("Please input method number:")
if(question_num == "1"):
    A = np.array([[9,12,-6,-3]
                ,[12,41,2,11]
                ,[-6,2,24,-8]
                ,[-3,11,-8,62]])
    b = np.array([[-27],[-42],[32],[-23]])
    c = 163
    x = np.array([[1],[1],[1],[1]])
    H = np.eye(4)
    def function(x):
        return (1/2*np.dot(np.dot(x.T,A),x)+np.dot(b.T,x)+c)
    def df(x):
        return (np.dot(A,x)+b)
elif(question_num == "2"):
    A = np.array([[16,8,12,-12]
                ,[8,29,16,9]
                ,[12,16,29,-19]
                ,[-12,9,-19,35]])
    b = np.array([[7],[5],[-2],[9]])
    c = 5
    x = np.array([[1],[1],[1],[1]])
    H = np.eye(4)
    def function(x):
        return (1/2*np.dot(np.dot(x.T,A),x)+np.dot(b.T,x)+c)
    def df(x):
        return (np.dot(A,x)+b)
elif(question_num == "3"):
    x = np.array([[10],[20]])
    H = np.eye(2)
    # def function(x):
    #     return (x[0,0]-1)**2+10*(x[0,0]**2-x[1,0])**2
    # def df(x):
    #     return np.array([[40*pow(x[0,0],3)+2*x[0,0]-40*x[0,0]-2]
    #                     ,[20*x[1,0]-20*pow(x[0,0],2)]])
    A = np.array([[2,0]
                ,[0,20]])

    def function(x):
        return (1/2*np.dot(np.dot(x.T,A),x))
    def df(x):
        return (np.dot(A,x))


def linear_search (x1,x2,g,x,s):
    t = (-1 + math.sqrt(5))/2
    while x2-x1>0.001:
        alpha2 = t*(x2-x1)+x1
        alpha1 = t*t*(x2-x1)+x1
        if(g(x+alpha1*s)<g(x+s*alpha2)):
            x2 = alpha2
        else:
            x1 = alpha1
    return (alpha1)


if(method_num == "1"):
    count = 0
    s = -df(x)
    learning_rate = linear_search(0,1,function,x,s)
    x_ans = x-learning_rate*(df(x))

    while(np.linalg.norm(x_ans-x)>0.00001):
        x = copy(x_ans)
        s = -df(x)
        learning_rate = linear_search(0,1,function,x,s)
        x_ans += learning_rate*s
        count += 1

    print("＝＝最急降下法＝＝")
    print(x_ans)
    print(function(x_ans))
    print(count)

elif(method_num == "2"):
    count = 0
    s = -df(x)
    learning_rate = linear_search(0,1,function,x,s)
    x_ans = x+learning_rate*s

    while(np.linalg.norm(x_ans-x)>0.00001):
        x = copy(x_ans)
        learning_rate = linear_search(0,1,function,x,s)
        x_ans += learning_rate*s
        s = -df(x_ans)+s*(np.dot(df(x_ans).T,df(x_ans))/np.dot(df(x).T,df(x)))
        count += 1

    print("＝＝共役勾配法＝＝")
    print(x_ans)
    print(function(x_ans))
    print(count)

elif(method_num == "3"):
    count = 0
    s = -np.dot(np.linalg.inv(H),df(x))
    x_ans = x + s
    while(np.linalg.norm(x_ans-x)>0.001):
        y = df(x_ans)-df(x)
        H = H-np.dot(H,np.dot(s,np.dot(s.T,H)))/np.dot(s.T,np.dot(H,s))+np.dot(y,y.T)/np.dot(s.T,y)
        s = -np.dot(np.linalg.inv(H),df(x_ans))
        x = copy(x_ans)
        x_ans = x_ans+s
        count += 1

    print("＝＝準ニュートン法＝＝")
    print(x_ans)
    print(function(x_ans))
    print(count)
