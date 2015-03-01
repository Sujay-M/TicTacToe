import numpy as np
def sigmoid(z):
	sig = 1/(1+np.exp(-z))
	return sig
def cost(X,Y,theta):
	m,_ = X.shape
	h = sigmoid(X.dot(theta))
	J = (-1/m)*(np.ones(1,m,np.uint8))*(y*np.log(h)+(1-y)*log(1-h))
	return J
def gradient(X,Y,theta):
	m,_ = X.shape
	h = sigmoid(X.dot(theta))
	g = (1/m)*(np.Transpode((h-y))*X)
	return g
def gradientDescent(gradient,theta,alpha):
	theta = theta - alpha*gradient
	return theta
	