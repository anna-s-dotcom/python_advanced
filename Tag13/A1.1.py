from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = fetch_california_housing()

print(data.DESCR)

print(data.feature_names)

df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"]=data.target

print(df)

feature_cols =df[['AveRooms']]
df = df[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']]


X_train, X_test, y_train, y_test=train_test_split(df[["AveRooms"]],
                                                    df["Population"],
                                                    test_size=0.2)
print(X_train.head())

degree=2

quad=PolynomialFeatures(degree=degree)

X_train_quad=quad.fit_transform(X_train)

X_test_quad=quad.fit_transform(X_test)

# print(X_train_quad)

nr=LinearRegression()
nr.fit(X_train_quad,y_train)

X_sort=X_train.sort_values(by="Population")
X_sort_quad=quad.fit_transform(X_sort)


y_pred=nr.predict(X_sort_quad)

fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(X_train["AveRooms"], y_train, color="b")
ax.scatter(X_test["AveRooms"], y_test, color="g")
ax.plot(X_sort["AveRooms"], y_pred,color="red")
ax.set_xlabel("AveRooms")
ax.set_ylabel("Population")
plt.show()
