from collections import defaultdict
import math


class edge:
    def __init__(self, weight):
        self.weight = weight

    def getWeight(self):
        return self.weight

    def setWeight(self, v):
        self.weight = v


class node:
    def __init__(self, bias, ID, aType='step'):
        self.bias = bias
        self.inputs = []
        self.weights = []
        self.aType = aType
        self.out = 0
        self.ID = ID

    def setInputs(self, inputs):
        self.inputs = inputs

    def actFunction(self, p):
        if self.aType == 'step':
            if p >= 0:
                return 1
            else:
                return 0

    def activate(self):
        p = 0
        for i in range(len(self.weights)):
            p += self.weights[i] * self.inputs[i]
        self.out = self.actFunction(p + self.bias)

    def getBias(self):
        return self.bias

    def __str__(self):
        return str(self.ID)


class network:
    def __init__(self):
        self.nodes = {}
        self.edges = defaultdict(list)
        self.outputs = []
        self.inputs = []
        self.activeNodes = {}

    def addNode(self, ID, bias):
        self.nodes[ID] = (node(bias, ID))

    def inputToNode(self, ID, inputVal):
        self.nodes[ID].setInputs(inputVal)

    def getAllNodes(self):
        return self.nodes

    def getBiasNode(self, ID):
        return self.nodes[ID].getBias()

    def connectEdge(self, tar, src):
        self.target = str(tar)
        self.src = str(src)
        self.edges[self.target].append(self.src)

    def getEdges(self, tar):
        # Returns Connections based on passed target
        target = str(tar)
        if self.edges[target] == []:
            return None
        return self.edges[target]

    def setOut(self, outputs):
        self.outputs = outputs

    def setIn(self, inputs):
        self.inputs = inputs

    def getInput(self):
        return self.inputs

    def step(self):
        for i in (self.nodes):
            if i in self.outputs:
                pass
            else:
                self.activeNodes[i] = self.nodes[i].activate()
        for i in self.outputs:
            for e in self.edges[str(i)]:
                try:
                    print(self.activeNodes[e[0]])
                except KeyError:
                    pass

    def getOut(self):
        ret = []
        for i in range(len(self.outputs)):
            ret.append(self.outputs[i].out)
        return ret


n = network()

# add nodes to network
# n.addNode(ID, bias, aType 'type')
n.addNode("i0", -50)
n.addNode("i1", -50)
n.addNode("o0", 0)

n.inputToNode("i0", -100000)
n.inputToNode("i1", -100000)

nodes = n.getAllNodes()
# Print each node id
# for i in nodes:
#     print(i)

# A -> C W = 0.5
# B -> C W = -0.1

# Connect Edges to network with weights
# n.connectEdge(target, (src, weight))
n.connectEdge("o0", ("i0", 1))  # W = 0.5
n.connectEdge("o0", ("i1", 1))  # W = -.1

# Set output/input nodes
n.setOut([nodes["o0"]])
n.setIn([nodes["i0"], nodes["i1"]])

# Check and make sure step works
print("OUTPUT BEFORE:", n.getOut())
n.step()
print("OUTPUT AFTER:", n.getOut())

# What are the edges of o0?
edges = n.getEdges("o0")
# print("Edges of o0:", edges[0][1])
