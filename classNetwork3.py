import math

class edge:
    def __init__(self, weight):
        self.weight = weight

    def getWeight(self):
        return self.weight

    def setWeight(self, v):
        self.weight = v

class node:
    def __init__(self, bias, ID, aType = 'step'):
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
            if p > 0:
                return 1
            else:
                return 0

    # def activate(self):
    #     p = 0
    #     for i in range(len(self.weights)):
    #         p += self.weights[i] * self.inputs[i]
    #     self.out = self.actFunction(p + self.bias)

    def activate(self):
        p = 0
        for i in range(len(self.inputs)):
            p += self.inputs[i]
        self.out = self.actFunction(p+self.bias)
        return self.out


    def getBias(self):
        return self.bias

    def __str__(self):
        return str(self.ID)

class network:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.outputNodes = []
        self.inputNodes = []

    def addNode(self, ID, bias):
        self.nodes[ID] = (node(bias, ID))

    def inputToNode(self, ID, inputVal):
        self.nodes[ID].setInputs(inputVal)

    def getAllNodes(self):
        return self.nodes

    def getBiasNode(self, ID):
        return self.nodes[ID].getBias()

    def connectEdge(self, tar, src):
        self.target = (tar)
        self.src = (src)
        # Try catch so first connection defines target in dictionary, all others are only appended
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

    def setOutputNodes(self, outputs):
        self.outputNodes = outputs

    def setInputNodes(self, inputs):
        self.inputNodes = inputs

    def getInput(self):
        return self.inputs

    def step(self):
        val = []
        for i in (self.inputNodes):
            i = str(i)
            val.append(self.nodes[i].activate())
        for i in (self.outputNodes):
            self.inputToNode(str(i), (val))
            self.nodes[str(i)].activate()

    def getOut(self):
        ret = []
        # for i in range(len(self.outputNodes)):
        #     ret.append(self.outputNodes[i].out)
        for i in (self.outputNodes):
            i = str(i)
            ret.append(self.nodes[i].out)
        return ret

n = network()

# add nodes to network
# n.addNode(ID, bias, aType 'type')
n.addNode("i0", 0)
n.addNode("i1", 0)
n.addNode("o0", 0)

n.inputToNode("i0", [0, 5])
n.inputToNode("i1", [-5])

nodes = n.getAllNodes()

n.connectEdge("o0", ("i0", 0.5)) # W = 0.5
n.connectEdge("o0", ("i1", -.1)) # W = -.1

# Set output/input nodes
n.setOutputNodes([nodes["o0"]])
n.setInputNodes([nodes["i0"], nodes["i1"]])

# Check and make sure step works
print("OUTPUT BEFORE:", n.getOut())
n.step()
print("OUTPUT AFTER:", n.getOut())
