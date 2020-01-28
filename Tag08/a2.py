import numpy as np
import random

#arr=np.random.randint(1,101,(3,5))- verkürzte Version
arr=np.random.randint(1,101,size=15).reshape(3,5)
print(arr)


#alle spalen
print("Spalten-Columns")
print(np.subtract.reduce(arr,axis=1))
print(np.subtract.reduce(arr,axis=1).shape)
print()


print("Zeilen- Rows")
print(np.subtract.reduce(arr,axis=0))
print(np.subtract.reduce(arr,axis=0).shape)
print()


print(np.negative(arr))
