#k = (a,b)
from sympy import Inverse


def encrypt(m, p, a, b):

    #Encryption Formula
    e = ((a*m)+b) % p

    return e

def decrypt(c, p, a, b):

    #Computes modular inverse
    inverse = modInverse(a, p)

    #Decryption formula
    d = (inverse * (c - b)) % p

    return d 

#Just to use because I can
def modInverse(a, p):
    return pow(a, -1, p)

#For problem #2
print(encrypt(204, 541, 34, 71))
print(decrypt(431, 541, 34, 71))

print(modInverse(123, 4567))



