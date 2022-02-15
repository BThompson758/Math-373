#k = (a,b)
def encrypt(m, p, a, b):
    e = ((a*m)+b) % p

    return e

def decrypt(c, p, a, b):
    inverse = pow(a, -1, p)
    d = (inverse * (c - b)) 

    return d % p

print(encrypt(204, 541, 34, 71))
print(decrypt(431, 541, 34, 71))

