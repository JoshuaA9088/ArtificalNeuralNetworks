import math
from Myro import *
from Graphics import *


data=getData("sampleData1.txt")
plotData(data)   

X=[d[0] for d in data]
Y=[d[1] for d in data]

for i in range