import numpy as np
import tflearn
import matplotlib.pyplot as plt

def train_network(x, y, n_epoch=2000, LR=0.01):
    input_ = tflearn.input_data(shape=[None])
    linear = tflearn.single_unit(input_)
    neural_net = tflearn.regression(linear, optimizer='sgd', loss='mean_square',
                                metric='R2', learning_rate=LR)

    model = tflearn.DNN(neural_net, tensorboard_verbose=3)

    model.fit(x, y, n_epoch, snapshot_epoch=False)

    return model

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

data=getData("sampleData4.txt")

x=[d[0] for d in data]
y=[d[1] for d in data]

orModel = train_network(x, y, 10000, .03)

yHat = orModel.predict([i for i in x])

plt.scatter(x, y, c="red", marker="o")
plt.plot(x, yHat)
plt.show()