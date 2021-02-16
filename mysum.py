#!/usr/bin/python3

def mysum(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result

if __name__=='__main__':
    a = [1,2,3]
    b = [0]
    c = [-1, 2]
    print(sum(a) == mysum(*a))
    print(sum(b) == mysum(*b))
    print(sum(c) == mysum(*c))
