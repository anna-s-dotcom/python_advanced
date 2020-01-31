import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("autos.csv")
#fragezeichen ersetzen , thousands wie im Excel 1.000,05

df=pd.read_csv("autos.csv", na_values="?", thousands=None, decimal=".")

print(df)
# print(df.head())

print(df.columns)

# Index(['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration',
#        'num-of-doors', 'body-style', 'drive-wheels', 'engine-location',
#        'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type',
#        'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke',
#        'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg',
#        'highway-mpg', 'price'],
#       dtype='object')

#feature_cols=['horsepower','peak-rpm','city-mpg', 'highway-mpg',"price"]
feature_cols=['horsepower','city-mpg']
target_col="price"
df=df[['horsepower','peak-rpm','city-mpg', 'highway-mpg',"price"]]
#tutaj chyba usunelismy bledne wartosci
df=df.dropna()

# print(df.isna().any())
# print(df.isna().sum())


features=df[feature_cols].copy()
target=df[target_col].copy()
#
# pd.plotting.scatter_matrix(
#                             df,
#                             c=target,
#
#                             )
#
# plt.show()
# wenn ich die Korellation sehe, dann nehme ich es als Beispiel
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test=train_test_split(features, target,test_size=0.20)

lr=LinearRegression()
lr.fit(X_train,y_train)

print(f"Intercept:", lr.intercept_)
print("Anstieg:", lr.coef_)
print(f"R2 Score", lr.score(X_train, y_train))
print(f"R2 Score", lr.score(X_train, y_test))

# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.scatter(X_train,y_train)
# ax.plot(X_train, lr.predict(X_train), color="r")
#
#
# plt.show()

from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=fig.add_subplot(111, projection="3d")
ax.scatter(features["horsepower"],
            features["city-mpg"],
            features["city-mpg"],
            target)
ax.plot(X_train,)
