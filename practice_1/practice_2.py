'''def square(x):
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
'''

def sum_all(x):
    print(x)
    def next_sum(y):
        return sum_all(x+y)
    return next_sum

sum_all(1)(2)(3)

f1 = sum_all(1)
f2 = f1(2)
f3 = f2(3)

def split(n):
    return n//10 , n%10

def get_sum(n):
    if n <= 9:
        return n
    else:
        allbutlast,last=split(n)
        return get_sum(allbutlast) + last

def luhn_sum(n):
    if n <= 9:
        return n
    else:
        allbutlast,last = split(n)
        return luhn_double(allbutlast) + last
    
def luhn_double(n):
    allbutlast,last = split(n)
    nlast_double = last*2
    
    return luhn_sum(allbutlast) + get_sum(nlast_double)

print(luhn_sum(2))
print(luhn_sum(322))
print(luhn_sum(32))
print(luhn_sum(5105105105105100))
