import numpy as np

####reduce
#
# array=np.arange(1,10).reshape(3,3)
# print(array)
#
# print(np.add.reduce(array,axis=0))
# print(np.add.reduce(array,axis=0).shape)
# print()
#
# print(np.add.reduce(array,axis=1, keepdims=True))
# print(np.add.reduce(array,axis=1,keepdims=True).shape)
# print()

###accumulate


arr=np.arange(1,7).reshape(2,3)

print(arr)
print(arr.shape)
print()

print(np.add.accumulate(arr,axis=0))
print(np.add.accumulate(arr,axis=0).shape)
print()

print(np.add.accumulate(arr,axis=1))
print(np.add.accumulate(arr,axis=1).shape)
print()
