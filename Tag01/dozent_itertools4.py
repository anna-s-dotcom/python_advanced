import itertools as it

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c', 'd']

z = zip(l1, l2)

print(list(z))

z = it.zip_longest(l1, l2, fillvalue = 4)
print(list(z))

print()
def func(x):
    return x**2

lis = [1, 2, 3]

quad = map(func, lis)
print(list(quad))

def func2(a, b):
    return a*b

lis2 = [(1, 1),(2, 4),(3, 6)]

starquad = it.starmap(func2, lis2)
print(list(starquad))
