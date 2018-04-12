import numpy as np
import matplotlib.pyplot as plt

def getData(filename):
    data=[]
    f=open(filename)
    for line in f:
        line=line.split()
        for i in range(len(line)):
            line[i]=float(line[i])
        #print(line)
        data.append(line)
    return data

data = getData("sampleData1.txt")
# x = np.array(for d[0] in data)
# y = np.array([for d[1] in data])
for d in data:
    x.append([x])

plt.scatter(x, y, s=120, c=None, marker='o')

plt.show()
