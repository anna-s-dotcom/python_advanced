import itertools as it

lis = [2, 3, 2, 5, 3]

acc = it.accumulate(lis)

print(lis)
print(list(acc))

def mul(a, b):
    return a*b

acc = it.accumulate(lis, mul)
print(list(acc))
print()

################################
def get_state(person):
    return person['state']

people = [
    {'name': 'Jane', 'state': 'NY'},
    {'name': 'Joe', 'state': 'NY'},
    {'name': 'Jerry', 'state': 'WY'},
    {'name': 'Jeremy', 'state': 'WY'},
    {'name': 'Jacob', 'state': 'NY'}
]

person_group = it.groupby(people, get_state)

for key, group in person_group:
    print(key, group)
    for person in group:
        print(person)
    print('-------------')

lis = [1, 2, 85]

lists = it.tee(lis, 3)
# l1, l2, l3 = it.tee(lis, 3)

for l in lists:
    print(list(l))
