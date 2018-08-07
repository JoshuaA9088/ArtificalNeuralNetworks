import time
import numpy as np
import tflearn
import matplotlib.pyplot as plt
import os.path


def train_network(x, y, n_epoch=2000, LR=0.01, loadModel=None, retrain=False):
    input_ = tflearn.input_data(shape=[None])
    linear = tflearn.single_unit(input_)
    neural_net = tflearn.regression(linear, optimizer='sgd', loss='mean_square',
                                metric='R2', learning_rate=LR)

    model = tflearn.DNN(neural_net, tensorboard_verbose=3)

    if os.path.isfile(loadModel+".index"):
        try: 
            model.load(loadModel)
            if retrain:
                print("Successfully loaded old model. Forcing retrain!")
                model.fit(x, y, n_epoch, snapshot_epoch=False)
                return model

            print("Successfully loaded old model. Skipping training...")
            return model
        except:
            model.fit(x, y, n_epoch, snapshot_epoch=False)
            return model

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

def testRegress(dataPath, savePath, n_epochs=5000, LR=.01, retrain=False):
    data=getData(dataPath)

    x=[d[0] for d in data]
    y=[d[1] for d in data]
    
    model = train_network(x, y, n_epochs, LR, savePath, retrain)
    model.save(savePath)

    yHat = model.predict([i for i in x])

    plt.scatter(x, y, c="red", marker="o")
    plt.plot(x, yHat)
    plt.show()

# testRegress("sampleData.txt", "sample.model")
# testRegress("sampleData1.txt", "sample1.model")
# testRegress("sampleData3.txt", "sample3.model")
testRegress("sampleData4.txt", "sample4.model", 20000)#, retrain=True)
# testRegress("sampleData5.txt", "sample5.model", 200000)