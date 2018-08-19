import math
from classFinal import *

def andNetwork(val1, val2):
    n = network()

    n.addNode("i0", 0)
    n.addNode("i1", 0)
    n.addNode("o0", -1)

    n.inputToNode("i0", val1) # -> 0
    n.inputToNode("i1", val2) # -> -.1

    n.setInputNodes(["i0", "i1"])
    n.setOutputNodes(["o0"])

    n.connectEdge("o0","i0", 1) # W = 0.5
    n.connectEdge("o0","i1", 1) # W = -.1

    n.step()

    output = n.getOut()

    return output

def test():
    o1 = andNetwork(1, 0) # -> 0
    o2 = andNetwork(0, 1) # -> 0
    o3 = andNetwork(1, 1) # -> 1
    o4 = andNetwork(0, 0) # -> 0
    print(o1, "should be 0")
    print(o2, "should be 0")
    print(o3, "should be 1")
    print(o4, "should be 0")

test()