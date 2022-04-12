from sympy import false


def check(n,a,u,v):
    for x in (u-1):
     if(pow(pow(a,v),2*x, n) == -1):
        return false
    
check(1279,1091,1,639)