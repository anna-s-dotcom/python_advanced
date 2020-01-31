from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# mögliche methoden: .data , .target .feature_names .DESCR
# nicht .target_names   -> warum?

data = fetch_california_housing()

# print(data.DESCR)
print(data.feature_names)

# ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']

cols = ['MedInc', 'AveRooms']

# Scatter Matrix:
# pd.plotting.scatter_matrix(, c = data.target)
# plt.show()
