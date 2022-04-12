def isPrime(num):

    flag = 0

    for x in range(2, (num//2)+1):
  
        if (num % x) == 0:
            flag = 1

    if(flag == 0):
        print(num, "is prime")
    else:
        print(num, "is not prime")
            


