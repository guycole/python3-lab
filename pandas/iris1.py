# https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
# https://archive.ics.uci.edu/dataset/53/iris

import pandas as pd

#from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
#iris = fetch_ucirepo(id=53) 

data = pd.read_csv("uci_iris/iris.data", header=None) 
  
# data (as pandas dataframes) 
#X = iris.data.features 
#y = iris.data.targets 
  
# metadata 
#print(iris.metadata) 
  
# variable information 
#print(iris.variables) 

#print(type(iris))
print(data.head())
print(data.sample(10))