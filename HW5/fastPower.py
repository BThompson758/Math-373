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

#Calculates the remainder for g^a % m
for x in range(2, 2687):
    num = fastPower(x,1231,2687)
    if(num == 2565):
        print(x)
        break

fastPower(1774,1866,2687)
fastPower(1774,1231,2687)

fastPower(14, 11, 23)
print(fastPower(15, 12, 23))

#Prints result of fastPower
#print(num)

#Casts num into a string, and prints the sum of the digits
#print(sum([int(digit) for digit in str(num)]))

