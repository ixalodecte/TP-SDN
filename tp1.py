
from numpy import *
from sklearn import *
import sklearn.preprocessing as sp #pour iris 

iris = datasets.load_iris()
X = iris.data
Y = iris.target

def PPV(X,Y):
    R= 0,8*X.shape[0] #Nombre de données reference
    Ref = X[R:]
    Test= X[:R]
    for i in Test:
           metrics.pairwise.euclidean_distances(Ref,i)
        
        

print('Hello World!')


    
