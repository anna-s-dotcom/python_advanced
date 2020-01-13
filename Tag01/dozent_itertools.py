import itertools as it

# endlos

counter = it.count(start = 5, step = 0.5)

print(next(counter))
print(next(counter))

print()
lis = [1, 2, 3]
cyc = it.cycle(lis)

print(next(cyc))
print(next(cyc))
print(next(cyc))
print(next(cyc))
print(next(cyc))
print(next(cyc))
print(next(cyc))

print()
rep = it.repeat(lis, times = 10)

print(next(rep))
print(next(rep))
print(next(rep))
print(next(rep))
print(next(rep))

# endlich
print()
comb = it.combinations(['a', 'b', 'c'], 2)
print('combination:', list(comb))

print()
per = it.permutations(['a', 'b', 'c'], 2)
print('permutation:', list(per))

print()
comb_wr = it.combinations_with_replacement(['a', 'b', 'c'], 2)
print('comb with rep:', list(comb_wr))

print()
prod = it.product(['a', 'b', 'c'], repeat = 2)
print('product:', list(prod))

print()
prod = it.product(['a', 'b', 'c'], [0, 1, 2])
print('product:', list(prod))
