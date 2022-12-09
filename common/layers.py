import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.functions import *


# Version for Backpropogation Gradient Descent Model
class Relu:
    def __init__(self):
        self.mask = None
    
    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0

        return out
    
    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx

class Sigmoid:
    def __init__(self):
        self.out = None
    
    def forward(self, x):
        out = sigmoid(x)
        self.out = out
        
        return out
    
    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out

        return dx

class Affine:
    def __init__(self, W, b):
        # initialize weight, bias from TwoLayerNet __init__
        self.W = W
        self.b = b

        # later going to use these variables
        self.x = None
        # self.original_x_shape = None
        # differentiate weight & bias
        self.dW = None
        self.db = None

    def forward(self, x):
        # tensor
        # self.original_x_shape = x.shape
        # x = x.reshape(x.shape[0], -1)

        self.x = x
        out = np.dot(self.x, self.W) + self.b

        return out

    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis = 0)

        # dx = dx.reshape(self.original_x_shape)

        return dx

class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None
        self.y = None
        self.t = None

    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)

        return self.loss

    def backward(self, dout=1):

        # batch_size = self.t.shape[0]
        # if self.t.size == self.y.size:
        #     dx = (self.y - self.t) / batch_size
        # else:
        #     dx = self.y.copy()
        #     dx[np.arange(batch_size), self.t] -= 1
        #     dx = dx / batch_size

        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size

        return dx
"""
# Version for Simple Multivariable Gradient Descent Model
class AddLayer:
    def __init__(self):
        pass

    def forward(self, x, y):
        out = x + y

        return out

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1

        return dx, dy

class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y

        return out

    def backward(self, dout):
        # swap x and y values for backward
        dx = dout * self.y
        dy = dout * self.x

        return dx, dy

class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0

        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx

class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out

        return out

    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out

        return dx

class Affine:
    def __init__(self, w, b):
        self.W = w
        self.b = b
        self.x = None
        self.dW = None
        self.db = None

    def forward(self, x, b):
        self.x = x
        out = np.dot(x. self.W) + b

        return out

    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis = 0)

        return dx

class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None
        self.y = None
        self.t = None

    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)

        return self.loss

    def backward(self, dout = 1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size

        return dx
"""