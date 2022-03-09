#g is base, a is power, m is mod
def fastPower(g, a, m):
 
    #initialize result
    result = 1

    #while the number is > 1
    while a > 0:

        #if power is odd, 
        if a % 2 == 1:
            result = (result * g) % m

        #Power is divided in half
        a = a // 2

        #Base becomes g^2 % m
        g = (pow(g,2,m))

    return result


