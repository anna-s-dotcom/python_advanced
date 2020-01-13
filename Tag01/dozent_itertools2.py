import itertools as it
import numpy as np

arr = np.array([1, 2, 3])
lis = ['a', 'b', 'c']
tup = (True, False)

ch = it.chain(arr, lis, tup, range(5, 8))

# for x in ch:
#     print(x)

print()
# it.islice(iterable, start, stop, step)
slice = it.islice(ch, 2, 8, 2)

for x in slice:
    print(x)
print()

lis = [1, 2, 3, 4]
b = [0, 1, 0, 1]
b2 = [True, False]
b3 = [0, 1, 0, 1, 1]

comp = it.compress(lis, b)
print(list(comp))
print()

comp = it.compress(lis, b2)
print(list(comp))
print()

comp = it.compress(lis, b3)
print(list(comp))
print()

def lt2(x):
    if x < 2:
        return True
    else:
        return False

lis = [0, 2, 5, 1, 0, 3]

filterresult = filter(lt2, lis)
print(list(filterresult))

falsefilter = it.filterfalse(lt2, lis)
print(list(falsefilter))
print()

take = it.takewhile(lt2, lis)
print(list(take))

drop = it.dropwhile(lt2, lis)
print(list(drop))
