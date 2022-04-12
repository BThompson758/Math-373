def EEA(a,b):
    #Accounts for A or B being 0
    if(a == 0):
        return (b, 0, 1)
    elif(b == 0):
        return (a, 1, 0)
    #Recursively calls EEA & assigns r, d, u, v, and q
    else:

        #Remainder
        r = b % a

        #Quotient
        q = b // a

        #GCD, u and v assigned to the recursive EEA call
        d, u, v = EEA(r, a)
        return d, v - (q * u), u


#Ints cleaned up
a = 1722971
b = 1711330
d, u, v = EEA(a,b)

#Prints & labels returned values
print(f'd = {d}')
print(f'u = {u}, v = {v}')

g, h, i = EEA(d, 32351977451572789)

print(f'g = {g}')
