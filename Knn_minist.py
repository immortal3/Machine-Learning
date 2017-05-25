from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np
import sys

class NearestNeighbor(object):
    def __init__(self):
        pass

    def train(self,X,Y):
        self.Xtrain = X
        self.Ytrain = Y

    def predict(self,X):
        numtrain = len(self.Xtrain)
        mindistance = sys.maxsize
        minlabel = 0
        for i in range(numtrain):
            distance = np.sum(np.abs(X - self.Xtrain[i]))
            #distance = np.sqrt(np.sum(np.abs(X - self.Xtrain[i])))
            if(distance < mindistance):
                mindistance = distance
                minlabel = i
        return self.Ytrain[minlabel]



digits = load_digits()
training_data = []
training_label = []
for x in range(1500):
    training_data.append(digits.images[x])
    training_label.append(digits.target[x])
nn = NearestNeighbor()
nn.train(training_data,training_label)
error = 0
for i in range(1500,1790):
    prediction = nn.predict(digits.images[i])
    #print ('real prediction',digits.target[1509],'prediction using Knn',prediction)
    if digits.target[i] != prediction:
        error = error + 1


print ('Total number of error : ',error)
print ('Percentage of errro : ',float(error)/float(290)*100)
