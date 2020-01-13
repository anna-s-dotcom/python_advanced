# Erstelle einen counter, der in 0.5 Schritten von 0 bis zu einem Endwert ausgibt.

def my_gen1(max):
    i = 0
    while i <= max:
        yield i
        i += 0.5

def my_gen2(max):
    for i in range(2*max+1):
        yield i*0.5

def my_gen3(max):
    for i in range(max):
        yield float(i)
        yield i + 0.5
    yield float(i+1)

def my_gen4(max):
    return (0.5*i for i in range(max*2+1))

gen1 = my_gen1(4)
print('my_gen1:')
for i in gen1:
    print(i)
print()

gen2 = my_gen2(4)
print('my_gen2:')
for i in gen2:
    print(i)
print()

gen3 = my_gen3(4)
print('my_gen3:')
for i in gen3:
    print(i)
print()

gen4 = my_gen4(4)
print('my_gen4:')
for i in gen4:
    print(i)
print()
