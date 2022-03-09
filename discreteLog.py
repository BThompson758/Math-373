def discreteLog(base, mod, result):
    for x in range(1, mod):
        if(pow(base, x, mod) == result):
            print(x)
            break

discreteLog(2, 1373, 893)