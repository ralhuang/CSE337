import re

filename = input("Filename: ")
ngram = int(input("What is your n value?"))

fileobject = open(filename, encoding='utf-8')

filestring = " ".join(("".join(fileobject.readlines())).split())
filestring = re.sub('[\^%$[#@!()+=*:,_&.\]]', "", filestring)
filearray = filestring.split()

indexoflongestngram = 0
longestngramlen = 0
ngrams = {}
for i in range(len(filearray) - ngram):
    counter = 0
    str = ""
    while(counter < ngram):
        str += (filearray[i + counter] + " ")
        counter += 1
    ngrams[i] = str

ngramarray = []
for index, str in ngrams.items():
    lentuple = (index, str, len(str))
    ngramarray.append(lentuple)

ngramarray.sort(key = lambda x: x[2], reverse = True)
print("Top 10 n-grams with highest length")

for i in range (0, 10):
    print(i, end = "")
    print(". " + ngramarray[i][1])
