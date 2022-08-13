from re import A


def fibo():
    a,b=0,1

    while True:
        yield a
        a,b=b,a+b

for i in fibo():
    if i>20:
        break
    else:
        print(i)