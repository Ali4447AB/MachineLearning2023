# -*- coding: utf-8 -*-
"""Untitled26.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wQ0KOlIe2N6OajogoXlcn_EKH2espAir
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions

https://drive.google.com/file/d/1r4RiNjXAlTfbNX3xGsOF1szm1VeTc0BG/view?usp=sharing

!pip install --upgrade --no-cache-dir gdown
!gdown 1r4RiNjXAlTfbNX3xGsOF1szm1VeTc0BG

# Load the dataset
data = pd.read_csv('/content/Perceptron.csv')
data

# Separate features and target
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Transforming y values from {-1, 1} to {0, 1}
y = np.where(y == -1, 0, 1)

# Splitting the dataset into the Training set and Test set (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
y

"""Loss"""

def bce(y, y_hat):
    eps = np.finfo(float).eps
    y_hat = np.clip(y_hat, eps, 1 - eps)
    return np.mean(-(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat)))

def mse(y, y_hat):
    return np.mean((y - y_hat)**2)

"""Accuracy"""

def accuracy(y, y_hat):
    acc = np.sum(y == y_hat) / len(y)
    return acc

"""Neuron"""

class Neuron:

    def __init__(self, in_features, threshold=-18, loss_fn=mse, n_iter=100, eta=0.1, verbose=True):
        self.in_features = in_features
        # weight & bias
        self.w = np.random.randn(in_features, 1)
        self.b = np.random.randn()
        self.threshold = threshold
        self.loss_fn = loss_fn
        self.loss_hist = []
        self.w_grad, self.b_grad = None, None
        self.n_iter = n_iter
        self.eta = eta
        self.verbose = verbose

    def activation_function(self, z):
        return np.where(z > self.threshold, 1, 0)

    def predict(self, x):
        # x: [n_samples, in_features]
        y_hat = x @ self.w + self.b
        y_hat = self.activation_function(y_hat)
        return y_hat

    def fit(self, x, y):
        for i in range(self.n_iter):
            y_hat = self.predict(x)
            loss = self.loss_fn(y, y_hat)
            self.loss_hist.append(loss)
            self.gradient(x, y, y_hat)
            self.gradient_descent()
            if self.verbose & (i % 1 == 0):
                print(f'Iter={i}, Loss={loss:.4}')

    def gradient(self, x, y, y_hat):
        self.w_grad = (x.T @ (y_hat - y)) / len(y)
        self.b_grad = (y_hat - y).mean()

    def gradient_descent(self):
        self.w -= self.eta * self.w_grad
        self.b -= self.eta * self.b_grad

    def __repr__(self):
        return f'Neuron({self.in_features}, {self.threshold})'

    def parameters(self):
        return {'w': self.w, 'b': self.b}

neuron = Neuron(in_features=2, loss_fn=bce, n_iter=100, eta=0.1, verbose=True)
perceptron_model=neuron.fit(X_train, y_train[:, None])
neuron.parameters()

plt.plot(neuron.loss_hist)

"""Evaluation"""

y_hat = neuron.predict(X_test)
accuracy(y_test[:, None], y_hat)

y_hat[:, 0], y_test

plot_decision_regions(X_train, y_train, clf=neuron, legend=2)

# Scatter plot for test data
plt.scatter(X_test[y_test == 0][:, 0], X_test[y_test == 0][:, 1], c='blue', marker='o', label='Class 0 (Test)')
plt.scatter(X_test[y_test == 1][:, 0], X_test[y_test == 1][:, 1], c='red', marker='o', label='Class 1 (Test)')

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Perceptron Classifier with Decision Boundary')
plt.legend()
plt.show()