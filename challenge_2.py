'''
Replace ith element with product of other elements

WITH DIVISION

a = [int(x) for x in input().split()]
b = []

def muck(a):
    tot = 1
    for i in a:
        tot *= i 

    return tot 

stuff = muck(a)

for i in a:
    b.append(stuff // i)

print(b)
'''


#WITHOUT DIVISION
a = [int(x) for x in input().split()]
b = []

def muck(a):
    tot = 1
    for i in a:
        tot *= i
    return tot 

for i in range(len(a)):
    tem = a.pop(i)
    k = muck(a)
    b.append(k)
    a.insert(i, tem)

print(b)

