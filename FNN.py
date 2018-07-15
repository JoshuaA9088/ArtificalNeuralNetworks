# import math
# import numpy as np


# class edge:
#     def __init__(self, weight):
#         self.weight = weight

#     def getWeight(self):
#         return self.weight

#     def setWeight(self, v):
#         self.weight = v

# class node:
#     def __init__(self, bias, ID, nodeType, aType = 'step'):
#         self.bias = bias
#         self.inputs = []
#         self.weights = []
#         self.nodeType = nodeType
#         self.aType = aType
#         self.out = 0
#         self.ID = ID

#     def setInputs(self, inputs):
#         self.inputs = inputs

#     def actFunction(self, p):
#         if self.aType == 'step':
#             if p > 0:
#                 return 1
#             else:
#                 return 0
#         if self.aType == 
#     # def activateAsOutput(self):
#     #     p = 0
#     #     for i in range(len(self.weights)):
#     #         p += self.weights[i] * self.inputs[i]
#     #     self.out = self.actFunction(p + self.bias)

#     # def activateAsInput(self):
#     #     self.out = self.inputs
#     #     return self.out

#     def activate(self):
#         if self.nodeType == "input":
#            self.out = self.inputs
#            return self.out

#         elif self.nodeType == "output":
#             p = 0
#             for i in range(len(self.weights)):
#                 p += self.weights[i] * self.inputs[i]
#             self.out = self.actFunction(p + self.bias)

#     def getBias(self):
#         return self.bias

#     def setWeights(self, weight):
#         self.weights.append(weight)

#     def __str__(self):
#         return str(self.ID)

# class network:
#     def __init__(self):
#         self.nodes = {}
#         self.edges = {}
#         self.outputNodes = []
#         self.inputNodes = []
#         self.hiddenNodes = []

#     def addNode(self, ID, bias, nodeType):
#         self.nodes[ID] = node(bias, ID, nodeType)
#         if nodeType == "input":
#             self.inputNodes.append(ID)
#         elif nodeType == "output":
#             self.outputNodes.append(ID)
#         elif nodeType == "hidden":
#             self.hiddenNodes.append(ID)

#     def inputToNode(self, ID, inputVal):
#         self.nodes[ID].setInputs(inputVal)

#     def getAllNodes(self):
#         return self.nodes

#     def getBiasNode(self, ID):
#         return self.nodes[ID].getBias()

#     def connectEdge(self, tar, src, weight):
#         self.target = (tar)
#         self.src = (src)
#         # Try catch so first connection defines target in dictionary, all others are only appended
#         try:
#             self.edges[self.target]
#         except:
#             self.edges[self.target] = []
#         self.edges[self.target].append(self.src)
#         self.nodes[self.target].setWeights(weight)

#     def getEdges(self, tar):
#         # Returns Connections based on passed target
#         target = str(tar)
#         try:
#             self.edges[target]
#         except:
#             return "Undefined Target"
#         return self.edges[target]

#     # def setOutputNodes(self, outputs):
#     #     self.outputNodes = outputs

#     # def setInputNodes(self, inputs):
#     #     self.inputNodes = inputs

#     def getInput(self):
#         return self.inputNodes

#     def step(self):
#         val = []
#         for i in (self.inputNodes):
#             i = str(i)
#             val.append(self.nodes[i].activate())
#         for i in (self.outputNodes):
#             i = str(i)
#             self.inputToNode(i, (val))
#             self.nodes[i].activate()

#     def getOut(self):
#         ret = []
#         for i in (self.outputNodes):
#             i = str(i)
#             ret.append(self.nodes[i].out)
#         return ret


# # def sigmoid(x):
# #     return 1/(1 + np.exp(-x))

# # def feedForward():
# #     layer1 = sigmoid(np.dot(input, weights1))
# #     output = sigmoid(np.dot(layer1, weights2))


# def test(x1, x2):
#     n = network()
#     # addNode("ID", bias, type)
#     n.addNode("i0", 1, "input")
#     n.addNode("i1", 1, "input")
#     n.addNode("o0", 0, "output")

#     # inputToNode("ID", singleInt)
#     n.inputToNode("i0", x1)
#     n.inputToNode("i1", x2)

#     # connectEdge("targetID", "srcID", weight)
#     n.connectEdge("o0","i0", 1) # W = 0.5
#     n.connectEdge("o0","i1", 1) # W = -.1

#     # Step activation
#     n.step()

#     output = n.getOut()

#     return output


# def FNN(x1, x2):
#     n = network()
    
#     n.addNode("i0", 0, "input")
#     n.addNode("i1", 0, "input")

#     n.addNode("h0", 0, "hidden")
#     n.addNode("h1", 0, "hidden")
    
#     n.addNode("o0", 1, "output")

#     n.inputToNode("i0", x1)
#     n.inputToNode("i1", x2)

#     n.connectEdge("i1", "i0", 1)
#     n.connectEdge("h0", "i1", 1)
#     n.connectEdge("h1", "i0", 1)
#     n.connectEdge("o0", "h0", 1)
#     n.connectEdge("o0", "h1", 1)
    
#     n.step()

#     output = n.getOut()

#     return output

# def xor():
#     a = FNN(0, 0)
#     b = FNN(0, 1)
#     c = FNN(1, 0)
#     d = FNN(1, 1)

#     if a == 0 and b == 0:
#         if b == 1 and c == 1:
#             print("passed")

#     print(a, b, c, d)
# if __name__ == "__main__":
#     xor()


# # Types: "input", "output", "hidden"