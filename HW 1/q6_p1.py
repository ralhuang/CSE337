import math

for i in range(100, 1000):
    strvalue = str(i)
    power = len(strvalue)
    sumvalue = 0
    for j in range(0, power):
        nvalue = lambda x: math.pow(x, power)
        sumvalue += nvalue(int(strvalue[j]))
    if sumvalue == i:
        print(i)
