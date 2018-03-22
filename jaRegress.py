from Graphics import *
import math

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





def linearRegression(X, y, m_current=0, b_current=0, epochs=1000, learning_rate=0.0001):
     N = float(len(y))
     for i in range(epochs):
          y_current = (m_current * X) + b_current
          cost = sum([data**2 for data in (y-y_current)]) / N
          m_gradient = -(2/N) * sum(X * (y - y_current))
          b_gradient = -(2/N) * sum(y - y_current)
          m_current = m_current - (learning_rate * m_gradient)
          b_current = b_current - (learning_rate * b_gradient)
     return m_current, b_current, cost          

    
        
    
data=getData("sampleData.txt")
plotData(data)   

X=[d[0] for d in data]
Y=[d[1] for d in data]
    
b0, b1 = linearRegression(X, Y)
print (b0, b1)