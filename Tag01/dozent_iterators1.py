class Iterable:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.end:
            raise StopIteration
        # self.value += 1
        # return self.value-1
        current = self.value
        self.value += 1
        return current

it = Iterable(1, 5)

# print(next(it))
# print(it.__next__())
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for i in it:
    print(i)
