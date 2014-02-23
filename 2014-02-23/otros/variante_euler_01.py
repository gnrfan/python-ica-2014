#! usr/bin/env python
# Contribuído por José.

def divisible(a,b):
    return a % b == 0

if __name__ == '__main__':
    acum = 0
    for n in range(1, 1000):
        if (divisible(n,3)):
            #print x
            #print '\n'
            acum += n
        elif (divisible(n,5)):
            acum -= n
    print acum
