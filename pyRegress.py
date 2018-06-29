import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
import matplotlib.pyplot as plt


class Regression(nn.Module):

    def __init__(self, input_dim, output_dim):
        super(Regression, self).__init__()
        # Super class constructor
        self.linear = nn.Linear(input_dim, output_dim)
        print(self.linear)
        # input()
    def forward(self, x):
        # Simple y = mx+b calc function
        out = self.linear(x)
        return out

class fitLine:
    def __init__(self):
        self.input_dim = 1
        self.output_dim = 1
        pass

    def setVals(self, x, y):
        self.x_vals = x
        self.y_vals = y
        self.x_train = np.asarray(self.x_vals,dtype=np.float32).reshape(-1,1) # Reformats array
        self.y_actual = np.asarray(self.y_vals,dtype=np.float32).reshape(-1,1)

    def regress(self, epochs=2000):
        model = Regression(self.input_dim, self.output_dim)
        msl = nn.MSELoss() # Mean Squared Loss
        learning_rate = 0.01
        optimiser = torch.optim.SGD(model.parameters(), lr = learning_rate)

        # epochs = 2000

        for epoch in range(epochs):

            self.inputs = Variable(torch.from_numpy(self.x_train))
            self.labels = Variable(torch.from_numpy(self.y_actual))

            # clear grads
            optimiser.zero_grad()

            self.outputs = model.forward(self.inputs)
            self.loss = msl(self.outputs, self.labels)
            self.loss.backward() # backprop
            optimiser.step()
            print('epoch {}, loss {}'.format(epoch, self.loss.data[0]))

        self.predicted = model.forward(Variable(torch.from_numpy(self.x_train))).data.numpy()

        plt.plot(self.x_train, self.y_actual, "go", label = "from data", alpha = .5) # Scatter plot actual data
        plt.plot(self.x_train, self.predicted, label = "prediction", alpha = .5) # Draw line of predicted
        plt.legend()
        plt.show()
        print(model.state_dict())

if __name__ == "__main__":
    print("Local Run")
