def trc1(g):
    def wrapper(x):
        print("Calling", g, "on argument", x)
        return g(x)
    return wrapper

@trc1
def sqr(x):
    return x*x

@trc1
def sum_sqr(n):
    sum = 0
    for i in range(1, n+1):
        sum += sqr(i)
    return sum


print(sqr(3))
print(sum_sqr(3))


  			
