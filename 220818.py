g = lambda x, y : x * y
print(g(2, 3))
print(g(3, 4))

#recursive
def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)

print(factorial(3))

help(print)