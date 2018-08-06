from Graphics import *
from math import sqrt

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


def drawLine(x0,x1):
    line=[]
    for i in range(0,win.width,step):
        yHat=x0+x1*i        
        c=Circle((i,getY(yHat)),5)
        c.fill=Color("green")
        c.draw(win)
        line.append(c)
    return line        

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
    
def gradientDescent(b0,b1,d):
    lRate=0.01
    yHat=b0+b1*d[0]
    error=yHat-d[1]
    print("error is ",error)
    b0=b0-lRate*error
    b1=b1-lRate*error*d[0]
    print(b0,b1)
    return b0,b1   
       
    
data=getData("sampleData1.txt")
plotData(data)   

X=[d[0] for d in data]
Y=[d[1] for d in data]

b1=0
b0=0
    

#drawLine(450,-0.8)
line=drawLine(b0,b1)

while True:
    for l in line:
        l.undraw()
    drawLine(b0,b1)
        
    for d in data:
        b0,b1=gradientDescent(b0,b1,d)
    
    print(b0,b1)
    
    ans=input("Press any key to continue")
    if ans=='q':
        break
    
    
    
    
    
