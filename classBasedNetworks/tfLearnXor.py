from tflearn import DNN
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import time
import datetime

date = str(datetime.datetime.now()).split('.')[0][-8:]

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y = [[0], [1], [1], [0]]

input_layer = input_data(shape=[None, 2])
hidden_layer = fully_connected(input_layer, 2, activation='tanh')
output_layer = fully_connected(hidden_layer, 1, activation='tanh')

regression = regression(output_layer, optimizer='sgd',
                        loss='binary_crossentropy', learning_rate=5)
model = DNN(regression, tensorboard_verbose=3)

model.fit(X, Y, n_epoch=2000, show_metric=True, run_id=date)

print([i[0] > 0 for i in model.predict(X)])
