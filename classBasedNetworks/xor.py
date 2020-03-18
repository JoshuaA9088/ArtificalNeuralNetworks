# -*- coding: utf-8 -*-
from NN import network


def xor(val1, val2):
    n = network()

    n.addNode("a", 0)
    n.addNode("b", 0)

    n.addNode("c", 0)
    n.addNode("d", 0)

    n.addNode("o0", 0)

    n.setInputNodes(["a", "b", "c", "d"])
    n.setOutputNodes(["o0"])

    n.inputToNode("a", val1)  # -> 0
    n.inputToNode("b", val2)  # -> -.1

    n.connectEdge("c", "a", 1)
    n.connectEdge("c", "b", 1)

    n.connectEdge("d", "a", 1)
    n.connectEdge("d", "b", 1)

    n.connectEdge("o0", "c", 1)  # W = 0.5
    n.connectEdge("o0", "d", 1)  # W = -.1

    n.step()

    return n.getOut()


def test():
    o1 = xor(1, 0)  # -> 1
    o2 = xor(0, 1)  # -> 1
    o3 = xor(1, 1)  # -> 1
    o4 = xor(0, 0)  # -> 0

    assert o1 == [1]
    assert o2 == [1]
    assert o3 == [1]
    assert o4 == [0]


test()


"""

If I remember correctly, a 2 layer, 2 input node
linear perceptron cannot solve xor.

More research needed.

INPUT	OUTPUT
A	B	A xor B
0	0	1
0	1	1
1	0	1
1	1	0
"""
