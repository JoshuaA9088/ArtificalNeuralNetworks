import time
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import os.path

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train)
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# Define architecure of model
model = tf.keras.models.Sequential()  # Sequential is feed-forward
model.add(tf.keras.layers.Flatten())  # Input layer
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # Hidden layer 1
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # Hidden layer 2
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))  # Output Layer

# adam optimizer is kinda go-to, can use stohcatic GD
# Loss, use this one!
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy", metric=["accuracy"])

model.fit(x_train, y_train, epochs=3)

predictions = model.predict([x_test])  # Returns propability spread

print(np.argmax(predictions[0]))
plt.imshow(x_test[0])
plt.show()
