import time
import numpy as np
import tensorflow as tf
import tflearn
import matplotlib.pyplot as plt
import os.path
import datetime

date = str(datetime.datetime.now()).split('.')[0][-8:]
date = date.replace(":", ".")


def train_network(x, y, n_epoch=2000, LR=0.01, loadModel=None, retrain=False):
    tf.reset_default_graph()
    input_ = tflearn.input_data(shape=[None])
    linear = tflearn.single_unit(input_)
    neural_net = tflearn.regression(linear, optimizer='sgd', loss='mean_square', metric='R2', learning_rate=LR)

    model = tflearn.DNN(neural_net, tensorboard_verbose=3)

    if os.path.isfile(loadModel+".index"): # If the passed model name exists attempt to load it
        try: 
            model.load(loadModel)
            if retrain: # Force retrain given model
                print("Successfully loaded old model. Forcing retrain!")
                try:
                    m = list(loadModel)
                    m = m[m.index("/")+1:m.index(".")]
                    m = "".join(m)
                except:
                    m = 'Invalid_Name'
                ID = "tfLearn_Regress_"+ m + "_" + date
                model.fit(x, y, n_epoch, snapshot_epoch=False, run_id=ID)
                return model

            print("Successfully loaded old model. Skipping training...")
            return model

        except: # If model is not found, create it
            model.fit(x, y, n_epoch, snapshot_epoch=False, run_id=ID)
            return model

    model.fit(x, y, n_epoch, snapshot_epoch=False, run_id=ID)

    return model

def getData(filename):
    """
    Function to parse graph point txt files
    """

    data=[]
    f=open(filename)
    for line in f:
        line=line.split()
        for i in range(len(line)):
            line[i]=float(line[i])
        #print(line)
        data.append(line)
    f.close()
    return data

def testRegress(dataPath, savePath, n_epochs=5000, LR=.01, retrain=False):
    color = []

    data=getData(dataPath)

    x=[d[0] for d in data] # Parse each column of data txt
    y=[d[1] for d in data]
    color=[d[2] for d in data]
    
    # Convert the numerical color values to names compatible with matplotlib
    for i in (color): 
        if i == 1.0:
            temp = color.index(i)
            color[temp] = "red"
        elif i == 0.0:
            temp = color.index(i)
            color[temp] = "blue"

    # Train and save the model
    model = train_network(x, y, n_epochs, LR, savePath, retrain)
    model.save(savePath)

    # Calculate line based on model
    yHat = model.predict([i for i in x])
    
    # Plot all the data
    plt.scatter(x, y, c=color, marker="o")
    plt.plot(x, yHat)
    plt.title(savePath[:-6])
    plt.show()

testRegress("sampleData.txt", "models/sample.model", 2000, retrain=True)
testRegress("sampleData1.txt", "models/sample1.model", retrain=True)
testRegress("sampleData3.txt", "models/sample3.model", 10000, retrain=True)
testRegress("sampleData4.txt", "models/sample4.model", 10000, retrain=True)
testRegress("sampleData5.txt", "models/sample5.model", 10000, retrain=True)

# testRegress("testSet.csv", "testSet.model")