def gen():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'
    yield 'C'

obj = gen()
print(next(obj))

for i in obj:
    print(i)

