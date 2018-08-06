import numpy as np
import tflearn
import matplotlib.pyplot as plt

def train_network(x, y, n_epoch=2000, LR=0.01):
    input_ = tflearn.input_data(shape=[None])
    linear = tflearn.single_unit(input_)
    neural_net = tflearn.regression(linear, optimizer='sgd', loss='mean_square',
                                metric='R2', learning_rate=LR)

    model = tflearn.DNN(neural_net)

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

def testRegress():
    data=getData("sampleData3.txt")
    x=[d[0] for d in data]
    y=[d[1] for d in data]

    # x = [0., 1., 2., 3., 4., 5.]
    # y = [0., 2., 4., 6., 8., 10.]

    orModel = train_network(x, y, 4000, 0.01)

    yHat = orModel.predict([i for i in x])
    
    plt.scatter(x, y, c="red", marker="o")

    plt.plot(x, yHat)

    print(yHat)

    plt.show()

testRegress()
# testOr()