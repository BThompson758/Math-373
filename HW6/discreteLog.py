def discreteLog(base, mod, result):
    for x in range(1, mod):
        if(pow(base, x, mod) == result):
            print(x)
            break

discreteLog(14, 23, 22)
discreteLog(15, 23, 8)