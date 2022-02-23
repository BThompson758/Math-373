def isPrime(num):

    flag = 0

    for x in range(2, (num//2)+1):
  
        if (num % x) == 0:
            flag = 1

    if(flag == 0):
        print(num, "is prime")
    else:
        print(num, "is not prime")
            
isPrime(375997)
print(19157632841654891/375997)
print(39493517444969867/375997)
print(32351977451572789/375997)
