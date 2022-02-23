def findFactor(cipher):
    for x in range(2, cipher):
        if(cipher % x) == 0:
            return x
    return 0

def isPrime(num):

    flag = 0

    for x in range(2, num):
  
        if (num % x) == 0:
            flag = 1

    if(flag == 0):
        print(num, "is prime")
    else:
        print(num, "is not prime")
            

print(findFactor(39493517444969867))
isPrime(findFactor(39493517444969867))