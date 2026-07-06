def square(x):
    return x*x
def triple(x):
    return 3*x

def compose(f,g):
    def h(x):
        return f(g(x))
    return h

print(square(5))
print(triple(5))
squiple = compose(square,triple)
print(squiple(5))

a=1
def f(g):
    a=2
    return lambda y:a * g(y)
print(f(lambda y: a+y)(a))
