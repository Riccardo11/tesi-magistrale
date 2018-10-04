import numpy as np
from matplotlib import pyplot as plt


def sigmoid(x):
    return 1/(1+np.exp(-x))


def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


def tanh_derivative(x):
    return 1 - np.tanh(x)**2


X = np.arange(-10, 10.1, 0.25)

f, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(X, sigmoid(X))
ax1.plot(X, sigmoid_derivative(X), '--')
ax1.legend(['sigmoid', 'sigmoid derivative'])

ax2.plot(X, np.tanh(X))
ax2.plot(X, tanh_derivative(X), '--')
ax2.legend(['tanh', 'tanh derivative'])


# plt.legend()
plt.show()
