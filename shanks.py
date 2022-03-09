from math import isqrt
from fastPower import fastPower

m = 84298814015219
g = 2
h = 3

def shanks(g,h,m):

    #finds n
    n = 1 + isqrt(m-1)

    #Declares array with n location
    naive = [0] * n

    #Populates Naive 
    for x in range(n):
        naive[x] = fastPower(g,x,m)

    #flag for undefined
    sol = 0

    for y in range(n):
        #Computes List 2 Values
         giant = ((h * pow(pow(8,-1,m),n*y)) % m)

         #Compares giant to each value in List 1
         for z in range(n):
             if(giant == naive[z]):
                 sol = (z+(y*n))
             
    if(sol == 0):
        return "undefined"
    else:
        return sol

print(shanks(g,h,m))








