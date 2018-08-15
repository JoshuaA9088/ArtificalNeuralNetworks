# -*- coding: utf-8 -*-

""" Deep Neural Network for MNIST dataset classification task.
References:
    Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner. "Gradient-based
    learning applied to document recognition." Proceedings of the IEEE,
    86(11):2278-2324, November 1998.
Links:
    [MNIST Dataset] http://yann.lecun.com/exdb/mnist/
"""
from __future__ import division, print_function, absolute_import

import tflearn

# Data loading and preprocessing
import tflearn.datasets.mnist as mnist

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

def train_network(X, Y):
	# X, Y, testX, testY = mnist.load_data(one_hot=True)
	testX = X
	testY = Y

	# Building deep neural network
	input_layer = tflearn.input_data(shape=[None])
	dense1 = tflearn.fully_connected(input_layer, 64, activation='tanh',
									regularizer='L2', weight_decay=0.001)
	dropout1 = tflearn.dropout(dense1, 0.8)
	dense2 = tflearn.fully_connected(dropout1, 64, activation='tanh',
									regularizer='L2', weight_decay=0.001)
	dropout2 = tflearn.dropout(dense2, 0.8)
	softmax = tflearn.fully_connected(dropout2, 10, activation='softmax')

	# Regression using SGD with learning rate decay and Top-3 accuracy
	sgd = tflearn.SGD(learning_rate=0.1, lr_decay=0.96, decay_step=1000)
	top_k = tflearn.metrics.Top_k(3)
	net = tflearn.regression(softmax, optimizer=sgd, metric=top_k,
							loss='categorical_crossentropy')

	# Training
	model = tflearn.DNN(net, tensorboard_verbose=0)
	model.fit(X, Y, n_epoch=20, validation_set=(testX, testY),
	show_metric=True, run_id="dense_model")

	return model

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
    model = train_network(x, y)
    model.save(savePath)

    # Calculate line based on model
    yHat = model.predict([i for i in x])
    
    # Plot all the data
    plt.scatter(x, y, c=color, marker="o")
    plt.plot(x, yHat)
    plt.title(savePath[:-6])
    plt.show()

testRegress("sampleData3.txt", "perceptron3.model")

# print(Y)
# X, Y, testX, testY = mnist.load_data(one_hot=True)