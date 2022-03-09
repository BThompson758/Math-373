import fastPower

#finds the order

base = 8
mod = 211

for x in range(mod):
    if(fastPower(base, x, mod) == 1):
        print(x)
        break
