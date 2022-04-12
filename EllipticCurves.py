#Robert Thompson
#4/12/2022
#For MATH 373
from sympy import false, true

#Checks to see if the polynomial exists on E
def polynomial(x, y, a, b, field):
    if((pow(y,2) % field) == ((pow(x,3) + (a*x) + b) % field)):
        return true
    else:
        return false

#a,b pulled from equation E
def elliptic(x1, y1, x2, y2, mod, a, b):
    #Checks existance of equation on E
    if(polynomial(x1,y1,a,b,mod) == true):
        #Two slope checks, slope is for tangent line if equal
        if(x1 == x2 and y1 == y2):
            x = x1
            y = y1
            #Splits slope so inverse of denominator is possible
            slopeNumerator = (3*pow(x,2)+a) % mod
            slopeDenominator = (2*y) % mod
            if(slopeDenominator == 0):
                return print("Slope is Vertical")
            
            #Inverse of denominator
            inv = pow(int(slopeDenominator),-1,mod)

            #Calculates and prints Slope
            slope = (inv * slopeNumerator) % mod
            print(f'slope = {slope}')
        #When P1 and P2 are not equal
        else:
            #Checks P2 for existence on E
            if(polynomial(x2,y2,a,b,mod) == true):
                slopeNumerator = ((y2-y1) % mod)
                slopeDenominator = ((x2-x1) % mod)
                if(slopeDenominator == 0):
                    return print("Slope is Vertical")
                slope = slopeNumerator/slopeDenominator
                print(f'slope = {slope}')
            else:
                return print("P2 does not exist on curve E")

        #Equations for x3 and y3
        x3 = (pow(slope,2) - x1 - x2) % mod
        y3 = (slope * (x1 - x3) - y1) % mod
        print(f'(x3,y3) = ({x3},{y3})')
        return x3,y3
    else:
        return print("P1 does not exist on curve E")

x1,y1 = 1,2
x2,y2 = 1,-2

elliptic(x1,y1,x2,y2,100,2,1)

