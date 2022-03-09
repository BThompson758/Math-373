def computeCaps(g, lower, mod):
    return pow(g, lower, mod)

def computeKey(caps, lower, mod):
    return pow(caps, lower, mod)

a = 382114
b = 1744891346
mod = 918398656403699
g = 581330380946540
A = computeCaps(g, a, mod)
B = computeCaps(g, b, mod)
print(A)
print(B)

AKey = computeKey(B, a, mod)
BKey = computeKey(A, b, mod)

print(AKey)
print(BKey)