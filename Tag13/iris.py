from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn import metrics
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier



data = load_iris()
# scaler=MinMaxScaler()
# data_n=scaler.fit_transform(data.data)


df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"]=data.target


#df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     #columns= iris['feature_names'] + ['target'])

print(df)


knn=KNeighborsClassifier(n_neighbors=5)
# #['setosa' 'versicolor' 'virginica']
# #['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
features=df[["sepal length (cm)", "sepal width (cm)", "petal length (cm)","petal width (cm)"]].copy()
target=df["target"]
#
X_train, X_test, y_train, y_test=train_test_split(features, target,test_size=0.10)
#
knn.fit(X_train, y_train)

y_pred=knn.predict(X_test)
print(y_pred)
print("accuracy_score")
print(metrics.accuracy_score(y_test,y_pred))

print(pd.crosstab(y_test,y_pred,
                    rownames=["True"],
                    colnames=["Pred"]
                    ))

# print(data.DESCR) target=class, feature=eigenschaften
#print(data.target_names)
#print(data.feature_names)

#target als 0,1,2 codiert
#print(data.target)

#print()
#print(data.data)







#
# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.scatter(data.data[:,0],
#         data.data[:,1],
#         c=data.target,
#         cmap=plt.cm.summer)
#
# plt.show()
