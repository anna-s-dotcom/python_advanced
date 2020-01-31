import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
import numpy as np



data=load_iris()

features=data.data
target=data.target

scaler=MiniMaxScaler()
features=scaler.fit_transform(features)

X_train, X_test, y_train, y_test=train_test_split(features,
                                                    target,
                                                    test_size=0.1)
def logistic(x):
    return 1/(1+np.exp(-x))

x=np.arange(-5,5,0.05)

plt.plot(x,logistic(x))
plt.title("Logistische Funktion")
plt.show()
