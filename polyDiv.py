#Robert Thompson
#4/18/2022
#For MATH 373
import numpy as np

#3x^5+0x^4+0x^3+1x^2+0x,+1
a = np.poly1d([3,0,0,1,0,1])

#1x^3-1x^2+0x+2
b = np.poly1d([1,-1,0,2])


q,r = np.polydiv(a,b)

#Remember to look at things in terms of the Finite Field
#R gives -2x^2-6x-5 -> 3x^2-x+0 
#Matches what the calc was in class
print(q)
print(r)