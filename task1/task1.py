from sys import argv

n = int(argv[1])
m = int(argv[2])


def task1(n, m):
    yield 1
    for i in range(m-1, n*m, m-1):
        x = i % n + 1
        if x == 1:
            return
        yield x


result = list(task1(n, m))
total = int(''.join(map(str, result)))
print(total)









