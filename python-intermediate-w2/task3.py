def fib_generator(n):
    assert isinstance(n, (int, float)), "You should enter a number"
    i = 0
    fib_num = []
    while i <= 1 and i < n:
        fib_num.append(i)
        yield fib_num[i]
        i += 1
    if i > 1:
        while i < n:
            fib_num.append(fib_num[i-1]+fib_num[i-2])
            yield fib_num[i]
            i += 1

def fib_list(n):
    list = []
    for i in fib_generator(n):
        list.append(i)
    print(list)

fib_list(3)
