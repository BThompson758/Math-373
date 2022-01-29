def EAA(a,b):
    #Assume a>=b>=0
	#a > 0
		
	#Returns (d,u,v) such that d=GCD(a,b) and d=au + bv

    if(a == 0):
        return (b, 0, 1)
    else:
        gcd, u, v = EAA(b % a, a)
        return gcd, v - (b // a) * u, u

if __name__ == '__main__':
    gcd, u, v = EAA(30, 50)
    print('The GCD is ', gcd)
    print(f'u = {u}, v = {v}')