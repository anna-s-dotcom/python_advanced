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

# ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']

##########linear_model#############################
df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"]=data.target

print(df)

feature_cols =df[['AveRooms']]
df = df[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']]


# features = df[feature_cols].copy()
# target = df["target"].copy()

# pd.plotting.scatter_matrix(feature_cols, c=data.target)
# plt.show()

X_train, X_test, y_train, y_test=train_test_split(feature_cols, data.target,test_size=0.20)
#
lr=LinearRegression()
lr.fit(X_train,y_train)
print(f"Intercept:", lr.intercept_)
print(f'Anstieg:', lr.coef_)
print(f"Unsere Vorhersage: y = {lr.coef_[0]:.2f}*x + {lr.intercept_:.2f}")
print(f'R2 Score', lr.score(X_train, y_train))
print(f'R2 Score', lr.score(X_test, y_test))
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(X_train, y_train)
ax.plot(X_train, lr.predict(X_train), color = 'r')
plt.show()
