"""practice for higher order functions"""
from math import pi,sqrt
def area(r,shape_constant):
    assert r>0, 'the r is illegal'
    return r*r*shape_constant

def area_square(r):
    return area(r,1)

def area_circle(r):
    return area(r,pi)

def area_hexagon(r):
    return area(r,3*sqrt(3)*1/2)

def pow_diy(x,n):
    index=1
    total=x
    while index<n:
        total*=x
        index+=1
    return total

print(pow_diy(2,5))
print(pow_diy(2,3))

def cube(x):
    return pow_diy(x,3)

def naturals(x):
    return x

def sum_naturals(n):
    total,k= 0 ,1
    while k<=n:
        total,k=total+k,k+1
    return total

def sum_cubes(n):
    total,k=0,1
    while k<=n:
        total,k=total+pow(k,3),k+1
    return total

print(sum_naturals(5))
print(sum_cubes(3))

def summation(n,term):
    total,k=0,1
    while k<=n:
        total=total+term(k)
        k=k+1
    return total

print (summation(5,naturals))
print (summation(3,cube))

def make_adder(n):
    def adder(k):
        return k+n
    return adder

print(make_adder(3)(900))