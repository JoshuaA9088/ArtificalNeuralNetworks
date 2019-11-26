import math
from classFinal import *


def orNetwork(val1, val2):
    n = network()

    n.addNode("i0", 0)
    n.addNode("i1", 0)
    n.addNode("o0", 0)

    n.inputToNode("i0", val1)  # -> 0
    n.inputToNode("i1", val2)  # -> -.1

    n.setInputNodes(["i0", "i1"])
    n.setOutputNodes(["o0"])

    n.connectEdge("o0", "i0", 1)  # W = 0.5
    n.connectEdge("o0", "i1", 1)  # W = -.1

    n.step()

    output = n.getOut()

    return output


def test():
    o1 = orNetwork(1, 0)  # -> 1
    o2 = orNetwork(0, 1)  # -> 1
    o3 = orNetwork(1, 1)  # -> 1
    o4 = orNetwork(0, 0)  # -> 0
    print(o1, "should be 1")
    print(o2, "should be 1")
    print(o3, "should be 1")
    print(o4, "should be 0")


test()
