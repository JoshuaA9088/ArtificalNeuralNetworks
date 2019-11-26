from Graphics import *
from math import sqrt
from Myro import *


win = Window(500, 500)
step = 5
nue = 0.01


def mouseDown(o, e):
    print(e.x, e.y)


win.onMouseDown(mouseDown)


def getData(filename):
    data = []
    f = open(filename)
    for line in f:
        line = line.split()
        for i in range(len(line)):
            line[i] = float(line[i])
        # print(line)
        data.append(line)
    return data


def getY(y):
    return win.height - y


def mean(x):
    s = 0
    for i in range(len(x)):
        s += x[i]
    return s / len(x)


data = getData("sampleData5.txt")


X = [d[0] for d in data]
Y = [d[1] for d in data]

xAvg = mean(X)
yAvg = mean(Y)
for i in range(len(X)):
    X[i] = X[i] - xAvg
    Y[i] = Y[i] - yAvg


def plotData(data):
    color = None
    for d in data:
        if d[2] == 1:
            color = "red"
        else:
            color = "blue"
        c = Circle((d[0], getY(d[1])), 5)
        c.fill = Color(color)
        c.draw(win)


plotData(data)


def drawLine(m, b):
    # line=[]
    x1 = 0
    x2 = win.width
    y1 = m * x1 + b
    y2 = m * x2 + b
    foo = Line((x1, getY(y1)), (x2, getY(y2)))
    foo.draw(win)
    """
    for i in range(0,win.width,step):
        yHat=x0+x1*i
        c=Circle((i,getY(yHat)),5)
        c.fill=Color("green")
        c.draw(win)
        line.append(c)
    """

    return foo


def stddev(x):
    m = mean(x)
    s = 0
    for i in range(len(x)):
        s += pow(x[i] - m, 2)
    return sqrt(s / len(x))


def corr(X, Y):
    n = len(X)
    sumXY = 0
    sumX = 0
    sumY = 0
    sumX2 = 0
    sumY2 = 0

    for i in range(n):
        sumX += X[i]
        sumY += Y[i]
        sumXY += X[i] * Y[i]
        sumX2 += X[i] * X[i]
        sumY2 += Y[i] * Y[i]
    t = n * sumXY - sumX * sumY
    b = sqrt((n * sumX2 - pow(sumX, 2)) * (n * sumY2 - pow(sumY, 2)))

    r = t / b
    return r


def gradientDescent(m, b, X, Y):
    mRate = .00001
    bRate = .01
    n = len(X)
    bGradient = 0
    mGradient = 0
    cost = 0
    for i in range(n):
        yHat = (m * X[i]) + b
        error = abs(yHat - Y[i])
        mGradient += X[i] * (yHat - Y[i])
        bGradient += 1 * (yHat - Y[i])
        cost += pow((Y[i] - yHat), 2)
    mGradient = mGradient * (2.0 / n)
    bGradient = bGradient * (2.0 / n)
    cost = sqrt(cost) / n
    # print(cost)
    m = m - (mRate * mGradient)
    b = b - (bRate * bGradient)
    # print("bAfter", b)
    return m, b, cost


b = 0
m = 0

# drawLine(450,-0.8)
line = drawLine(m, b)

while True:
    line.undraw()

    m, b, cost = gradientDescent(m, b, X, Y)
    # m,b,cost = gradientDescent(b,X,Y)
    line = drawLine(m, b + yAvg)
    # print(X, Y)
    print(m, b, cost)
    wait(0.2)
    """
    ans=input("Press any key to continue")
    if ans=='q':
        break
    """
