from re import A

from isPrime import isPrime


def testing():

    N = 224769641117831
    A = 224769565124616

    p = 15893723
    q = 14151573

    isPrime(p)
    isPrime(q)

    print("224769565124616 = ")
    print((p-2)*(q-3))

    #print("224769641117831 = ") 
    #print(p*q)

    print("75993215 = ") 
    print((3*p)+(2*q))

testing()
