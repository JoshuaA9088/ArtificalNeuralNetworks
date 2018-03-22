from Graphics import *
from math import sqrt
from Myro import *
win=Window(500,500)
step=5
nue=0.01

def mouseDown(o,e):
    print(e.x,e.y)

win.onMouseDown(mouseDown)


def getData(filename):
    data=[]
    f=open(filename)
    for line in f:
        line=line.split()
        for i in range(len(line)):
            line[i]=float(line[i])
        #print(line)
        data.append(line)
    return data

def getY(y):
    return win.height-y
        
def plotData(data):
    color=None
    for d in data:
        if d[2]==1:
            color="red"
        else:
            color="blue"            
        c=Circle((d[0],getY(d[1])),5)
        c.fill=Color(color)
        c.draw(win)


def drawLine(m,b):
    #line=[]
    x1 = 0
    x2 = win.width
    y1 = m*x1 + b
    y2 = m*x2 + b
    foo = Line((x1, getY(y1)), (x2, getY(y2)))
    foo.draw(win)

    return foo        

def mean(x):
    s=0
    for i in range(len(x)):
        s+=x[i]
    return s/len(x)

def stddev(x):
    m=mean(x)
    s=0
    for i in range(len(x)):
       s+=pow(x[i]-m,2)
    return sqrt(s/len(x))
    
    
def corr(X,Y):
    n=len(X)
    sumXY=0
    sumX=0
    sumY=0
    sumX2=0
    sumY2=0
    
    for i in range(n):
        sumX+=X[i]
        sumY+=Y[i]
        sumXY+=X[i]*Y[i]
        sumX2+=X[i]*X[i]
        sumY2+=Y[i]*Y[i]
    t=n*sumXY-sumX*sumY
    b=sqrt((n*sumX2-pow(sumX,2))*(n*sumY2-pow(sumY,2)))
    
    r = t/b
    return r
  
def getError(c, yHat, y):
    if c == 1:
       error = (y - yHat)
    else:
       error = (yHat - y)
    return error 
          
def gradientDescent(m,b,X, Y, C):
    lRate=.000001
    n = len(X)
    bGradient = 0
    mGradient = 0
    cost = 0
    for i in range(n):
        yHat = (m * X[i]) + b
        error = getError(C[i], yHat, Y[i])
        mGradient += X[i] * (error)
        bGradient += 1*(error)
        #print(bGradient, "Bgrad")
        cost += pow((error),2)
    mGradient = mGradient * (-2/n)
    #bGradient = bGradient * (-2/n)
    cost = sqrt(cost) / n
    m = m - (lRate * mGradient)
    b = b - (lRate * bGradient)
    return m,b,cost, error


    
data=getData("sampleData1.txt")
plotData(data)   

X=[d[0] for d in data]
Y=[d[1] for d in data]
C = [d[2] for d in data]
b=0
m=0
    
#drawLine(450,-0.8)
line=drawLine(m,b)

while True:
    line.undraw()

    m,b,cost, error=gradientDescent(m,b,X, Y, C)
    line=drawLine(m,b)

    print(m,b, cost)
    print("Error", error)
    wait(0.3)
    """
    ans=input("Press any key to continue")
    if ans=='q':
        break
    """
    
    
    
    
