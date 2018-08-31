from Myro import *
from Graphics import *

win = Window(500, 500)

def mouseDown(o,e):
    f = open("regression\sampleData6.txt", "a")
    print(e.x,e.y)
    f.write(str(e.x) + ' ' + str(e.y) + ' 0')
    f.write('\n')
    c = Circle((e.x, e.y), 5)
    c.fill = Color("red")
    c.draw(win)
    f.close()

win.onMouseDown(mouseDown)
