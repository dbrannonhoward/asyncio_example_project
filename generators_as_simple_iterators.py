def countdown(n):
    while n > 0:
        yield n
        n -= 1


x = countdown(10)
for i in x:
    print(i)

x = countdown(2)
print(next(x))
print(next(x))
