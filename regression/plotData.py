from Graphics import *

win = Window(500, 500)


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


def plotData(data):
    color = None
    for d in data:
        if d[2] == 1:
            color = "red"
        else:
            color = "blue"
        c = Circle((d[0], d[1]), 5)
        c.fill = Color(color)
        c.draw(win)


def drawLine(x0, x1):
    step = 5
    for i in range(0, win.width, step):
        yHat = x0 + x1 * i
        c = Circle((i, yHat), 5)
        c.fill = Color("green")
        c.draw(win)


data = getData("sampleData1.txt")
plotData(data)
drawLine(450, -0.8)

print(data)
