import numpy as np
import scipy.optimize as op
import scipy.io as sio

def sigmoid(z):
	sig = 1/(1+np.exp(-z))
	return sig

def cost(theta,X,Y):
	m = len(X)
	h = sigmoid(X.dot(theta))
	J = (-1/m)*np.sum((Y*np.log(h)+(1-Y)*np.log(1-h)))
	return J

def gradient(theta,X,Y):
	m,n = X.shape
	theta = theta.reshape((n,1));
	Y = Y.reshape((m,1))
	h = sigmoid(X.dot(theta))
	g = (1/m)*(np.transpose((h-Y)).dot(X))
	return g

def gradientDescent(gradient,theta,alpha):
	theta = theta - alpha*gradient
	return theta

def createDataSet(n):
	X = np.zeros((n,9,9),np.uint8)
	Y = np.zeros((n,1),np.uint8)
	for i in range(n):
		[y,x] = tictactoe.main()
		for j in range(9):
			X[i,:,j] = x[j,:]
		Y[i,:] = y
	# np.save('X.npy',X)
	# np.save('Y.npy',Y)
	sio.savemat('X.mat',{'X':X})
	sio.savemat('Y.mat',{'Y':Y})
def predict(X,theta):
	n = len(X)
	print theta.shape
	X = X.reshape((1,n))
	theta = theta.reshape((n,1));
	h = sigmoid(X.dot(theta))
	return h
createDataSet(10000)
#loading data now
'''
X = np.load('X.npy')
Y = np.load('Y.npy')
m,n,_ = X.shape
X1 = np.ones((m,n+1,9),np.uint8)
X1[:,1:,:] = X
theta = np.zeros((9,n+1),np.double)
optimal_theta = np.zeros((9,n+1),np.double)
for i in range(9):
	
	# Result = op.minimize(fun = cost, x0 = theta[i,:], args = (X1[:,:,i], Y), method = 'TNC',
 #                                 jac = gradient);
	# optimal_theta[i,:] = Result.x;
	
	alpha = .01
	iterations = 500
	print 'for i = ',i
	for j in range(iterations):
		c = cost(theta[i,:],X1[:,:,i],Y)
		g = gradient(theta[i,:],X1[:,:,i],Y)
		theta[i,:] = gradientDescent(g,theta[i,:],alpha)
		print 'cost = ',c,' gradient = ',g
# print Result.message
np.save('theta.npy',optimal_theta)
'''