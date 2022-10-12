import numpy as np
import sys, os
sys.path.append(os.pardir) # allows us to bring files from parent directory
from dataset.mnist import load_mnist

# takes a few minutes when reading data for the first time
(x_train, t_train), (x_test, t_test) = load_mnist(flatten = True, normalize = False)

# check data shape
print(x_train.shape) # (60000, 784)
print(t_train.shape) # (60000, )
print(x_test.shape) # (10000, 784)
print(t_test.shape) # (10000, )

