#--------------------------------------
# Machine learnig in python
# Mário Jorge, june 2017
# Code exemple from http://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# Tested with anaconda 1.6.3 (python 3.6.1), sklearn 0.18.2, panda 0.20.1, matplotlib 2.0.0
#-----------------------------------


import pandas 
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#open datasets to explorer
#http://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/

#load dataset of iris
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url,names=names)

# printing the shape of the data
print ('shape (dataset.shape): ', dataset.shape)

#printing the head
print ('head (dataset.head): ', dataset.head)

#printing general simple analysis of the data (avg, mean...)
print('describe: ' , dataset.describe())

#print distribution of the feature
print ('groupby' , dataset.groupby('class').size())


# ----------- UNIVARIATE PLOTS -------------------
#box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()
#historiogram
dataset.hist()
plt.show()

# ----------- MULTIVARIATE PLOTS -------------------
scatter_matrix(dataset)
plt.show()

