def fibgen():
    a = 1
    b = 1
    yield 1
    yield 1
    while True:
        c = a + b
        yield c
        a = b
        b = c

fib = fibgen()

for i in range(8):
    print(next(fib))
