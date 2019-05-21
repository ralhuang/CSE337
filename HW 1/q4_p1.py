import re

filename = input("Filename: ")
ngram = int(input("What is your n value?"))

fileobject = open(filename, encoding='utf-8')
ngramdict = {}
filestring = " ".join(("".join(fileobject.readlines())).split())
filestring = re.sub('[\^%$[#@!()+=*:,_&.\]]', "", filestring)
filearray = filestring.split()

for i in range(len(filearray) - ngram):
    counter = 0
    str = ""
    while(counter < ngram):
        str += filearray[i + counter]
        counter += 1
    #print(str)
    if str in ngramdict:
        ngramdict[str] += 1
    else:
        ngramdict[str] = 1

print(ngramdict)
