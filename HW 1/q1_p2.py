import math
import statistics
import datetime

prices = {}
allprices = []

print("opening file")
with open("prices_sample.csv") as f:
        for line in f:
                if line[-1] == '\n':
                        line = line[:-1]
                (key, val) = line.split(',')
                x = datetime.datetime.fromtimestamp(int(key)).strftime('%Y-%m-%d %H:%M:%S')
                (day, ts) = (str(x)).split(' ')
                if day in prices:
                        prices[day].append(val)
                else:
                        prices[day] = [val]
                allprices.append(int(val))

allprices.sort()
percentiles = [.25, .50, .75]
u = statistics.mean(allprices)
print("Mean: " + str(u))
farthestprices = {}

for day in prices:
    if math.fabs(int(min(prices[day])) - int(u)) > math.fabs(int(max(prices[day])) - int(u)):
        farthestprices[day] = int(min(prices[day]))
    else:
        farthestprices[day] = int(max(prices[day]))

differences = []
for date, value in farthestprices.items():
    difftuple = (date, value, math.fabs(value - int(u)))
    differences.append(difftuple)

for y in percentiles:
    percentile = len(allprices) * y
    if isinstance(percentile, int):
        print(str(int(y * 100)) + "th Percentile: " + str(allprices[percentile]))
    else:
        print(str(int(y * 100)) + "th Percentile: " + str(allprices[int(int(percentile) + 0.5)]))
print("Variance: ", end = "")
print(statistics.pvariance(allprices))

differences.sort(key = lambda x: x[2], reverse = True)
for index in range(0, 6):
    print(str(differences[index][0]) + ": " + str(differences[index][1]))
