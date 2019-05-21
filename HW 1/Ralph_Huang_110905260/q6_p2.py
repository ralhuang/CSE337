import math

inputlist = [int(x) for x in input("Enter your numbers separated by spaces: \n").split()]
middlelist = list(map(lambda x: 2 ** x, inputlist))
outputlist = list(filter(lambda x: x < 1000, middlelist))

print(outputlist)
