from Graphics import *

win=Window(500,500)

def mouseDown(o,e):
    print(e.x,e.y)

win.onMouseDown(mouseDown)

