import functools

#def remap(checklist):


wordsAndCounts = {}
inputlist = [str(x) for x in input("list your words separated by spaces: \n").split()]
outputlist = []
for i in range(0, len(inputlist)):
    countlist = list(filter(lambda x : x == inputlist[i], inputlist))
    tuple = (inputlist[i], len(countlist))
    isInList = 0
    j = 0
    while j < len(outputlist):
        if outputlist[j] == tuple:
            isInList = 1
        j += 1
    if isInList == 0:
        outputlist.append(tuple)
print(outputlist)
