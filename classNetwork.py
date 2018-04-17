# Single Layer Neural Network

import math

class edge:
    def __init__(self, weight):
        self.weight = weight

    def getWeight(self):
        return self.weight

    def setWeight(self, v):
        self.weight = v

class node:
    def __init__(self, bias, aType = 'step'):
        self.bias = bias
        self.inputs = []
        self.weights = []
        self.aType = aType
        self.out = 0

    def setInputs(self, inputs):
        self.inputs = inputs

    def actFunction(self, p):
        if self.aType == 'step':
            if p >= 0:
                return 1
            else:
                return 0

    def addWeight(self, val):
        self.weights.append(val)

    def activate(self):
        p = 0
        for i in range(len(self.weights)):
            p += self.weights[i] * self.inputs[i]
        self.out = self.actFunction(p + self.bias)
        print("pou",self.out)

class network:
    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.outputs = []
        self.inputs = []

    def addNode(self, n):
        self.nodes.append(n)

    def connectEdge(self, tar, src):
        self.target = str(tar)
        # self.target = tar
        self.src = (src)
        # Try catch so first connection defines
        # target in dictionary, all others are only appended
        try:
            self.edges[self.target]
        except:
            self.edges[self.target] = []
        self.edges[self.target].append(self.src)

    def getEdges(self, tar):
        # Returns Connections based on passed target
        target = str(tar)
        try:
            self.edges[target]
        except:
            return "Undefined Target"
        return self.edges[target]

    def setOut(self, outputs):
        self.outputs = outputs

    def setIn(self, inputs):
        self.inputs = inputs

    def getInput(self):
        return self.inputs

    def step(self):
        for i in range(len(self.nodes)):
            self.nodes[i].activate()

    def getOut(self):
        ret = []
        for i in range(len(self.outputs)):
            ret.append(self.outputs[i].out)
        return ret

n = network()

# myNode = node(bias, aType = 'type')
a = node(-50)
b = node(-50)
c = node(0)


# add nodes to network
n.addNode(a)
n.addNode(b)
n.addNode(c)

# A -> C W = 0.5
# B -> C W = -0.1

# A        b
# \       /
#  \     /
#   \   /
#    \ /
#     C

# n.addEdge(target, (src, weight))

# Add Edges to network with weights
n.connectEdge(n.nodes[2], (n.nodes[0], 1)) # W = 0.5
n.connectEdge(n.nodes[2], (n.nodes[1], 1)) # W = -.1

a.addWeight(-10)
a.addWeight(-10)
a.setInputs([1, 1])

b.addWeight(1)
b.addWeight(1)
b.setInputs([1, 1])
# Set which node(s) are output and input
n.setOut([n.nodes[2]])
n.setIn([n.nodes[0], n.nodes[1]])



# Check and make sure step works
print(n.getOut())
n.step()
print(n.getOut())

edges = n.getEdges(n.nodes[2])
print(edges)
