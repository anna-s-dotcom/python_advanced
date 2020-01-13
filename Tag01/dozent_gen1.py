# def first_gen():
#     print('first time')
#     yield 1
#     print('second time')
#     yield 2
#     print('third time')
#     yield 3
#     print('fourth time')
#
# myfirstgen = first_gen()
#
# x = next(myfirstgen)
# print(x)
# next(myfirstgen)
# next(myfirstgen)
# next(myfirstgen)





import time
# liste:
t = time.time()
lc = [i**2 for i in range(1000000)]
print(time.time()-t)
print(type(lc))

# generator
t = time.time()
lc = (i**2 for i in range(1000000))
print(time.time()-t)
print(type(lc))

def sqr_gen():
    for i in range(1000000):
        yield i**2

t = time.time()
sqrs = sqr_gen()
print(time.time()-t)

t = time.time()
for x in sqrs:
    pass
print(time.time()-t)

t = time.time()
rgn = range(1000000)
print(time.time()-t)

# for x in sqrs:
#     print(x)
