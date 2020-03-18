# -*- coding: utf-8 -*-
from NN import network


def nandNetwork(val1, val2):
    n = network()

    n.addNode("i0", 0)
    n.addNode("i1", 0)
    n.addNode("o0", 0)

    n.inputToNode("i0", val1)  # -> 0
    n.inputToNode("i1", val2)  # -> -.1

    n.setInputNodes(["i0", "i1"])
    n.setOutputNodes(["o0"])

    n.connectEdge("o0", "i0", -1)  # W = 0.5
    n.connectEdge("o0", "i1", -1)  # W = -.1

    n.step()

    return n.getOut()


def test():
    o1 = nandNetwork(1, 0)  # -> 0
    o2 = nandNetwork(0, 1)  # -> 0
    o3 = nandNetwork(1, 1)  # -> 1
    o4 = nandNetwork(0, 0)  # -> 0

    assert o1 == [0]
    assert o2 == [0]
    assert o3 == [1]
    assert o4 == [0]


if __name__ == "__main__":
    test()

"""
INPUT	OUTPUT
A	B	A NAND B
0	0	1
0	1	1
1	0	1
1	1	0
"""
