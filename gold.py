import math
def No_1(x):
    return (1/x + math.exp(x))

def No_1_2(x):
    return (-(1/(x**2))+math.exp(x))

def No_1_3(x):
    return(2/(x**3) + math.exp(x))

def No_2(x):
    return (math.sin(5*x)+(x-5)**2)

def No_2_2(x):
    return (5*math.cos(5*x)+2*(x-5))

def No_2_3(x):
    return (-25*math.sin(5*x)+2)

def gold (x1,x2,g):
    count = 0
    t = (-1 + math.sqrt(5))/2
    while x2-x1>0.001:
        r1 = 0
        r2 = 0
        r2 = t*(x2-x1)+x1
        r1 = t*t*(x2-x1)+x1
        if(g(r1)<g(r2)):
            x2 = r2
        else:
            x1 = r1
        count +=1
    return (x1,x2,count)

def Bisec(x1,x2,g,g2):
    count = 0
    while x2-x1>0.001:
        tmp = (x1 + x2)/2
        if (g2(tmp)>0):
            x2 = tmp
        else :
            x1 = tmp
        count += 1
    return (x1,x2,count)

def Newton(x,g2,g3):
    count = 0
    t = x
    x = x - g2(x)/g3(x)
    while abs(x - t) >0.001:
        t = x
        x = x - g2(x)/g3(x)
        count += 1
    return (x,count)

print ("gold_1",gold(0,10,No_1))
print ("gold_2",gold(0,10,No_2))
print ("Bisec_1",Bisec(0,100,No_1,No_1_2))
print ("Bisec_2",Bisec(0,10,No_2,No_2_2))
print ("Newton_1", Newton(5,No_1_2,No_1_3))
print ("Newton_2",Newton(4.5,No_2_2,No_2_3))
