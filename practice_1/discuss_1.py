'''
"""is_prime?"""
from math import sqrt
def is_prime(n):
    if n==1:
        return False
    k=2
    while k<n and n%k!=0:
        k+=1
    if k==n:
        return True
    else :
        return False
k=1
while k<100 :
    if is_prime(k):print(k)
    k+=1
'''

'''
"""fizzbuzz?"""
def fizzbuzz(n):
    k=1
    while k<=n:
        if k%3==0 and k%5==0:
            print('fizzbuzz')
        elif k%3==0:
            print('fizz')
        elif k%5==0:
            print('buzz')
        else:
            print(k)
        k+=1

fizzbuzz(30)
'''

'''
"""ordered digits?"""
def ordered_digit(n):
    currd=n%10
    n=n//10
    pred=n%10
    while pred!=0:
        if pred>currd:
            return False
        else :
            currd=pred
            n=n//10
            pred=n%10
    return True

print(ordered_digit(5))
print(ordered_digit(11))
print(ordered_digit(127))
print(ordered_digit(1357))
print(ordered_digit(21))
print(ordered_digit(1375))
'''

'''
"""Unique Digits"""
def is_thesame(n,m):
    if n==m:
        return True
    else:
        return False

def how_many_times_k_in_num(k,num):
    digit=num%10
    num=num//10
    times=0
    while num!=0 or digit!=0:
        if is_thesame(k,digit):
            times+=1
        digit=num%10
        num=num//10
    return times

print(how_many_times_k_in_num(1,111))
print(is_thesame(3,5))
print(is_thesame(5,5))
print(how_many_times_k_in_num(1,1))

def unique_digits(n):
    k=1
    times_k=0
    num_uniq=0
    while k<10:
        times_k=how_many_times_k_in_num(k,n)
        if times_k==1:
            num_uniq+=1
        k+=1
    return num_uniq

print(unique_digits(1))
print(unique_digits(11))
print(unique_digits(111221))
print(unique_digits(123454321))
print(unique_digits(123456789))
'''

