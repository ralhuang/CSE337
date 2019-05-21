#It turns out looking at the prices in week-resolution could provide a higher-order summary of the price trends.
#Question. Write a program that computes the max, min, and the average prices for each and every week,
#and save it to a new file in a comma separated format. (YYYY-MM-DD followed by the values asked in the
#question, where YYYY-MM-DD is the first day of the week). You need to take into account incomplete weeks
#as well. [15 pts]

import datetime

prices = {}
minmaxave = {}
weeks = {}
print("Opening file")
with open("prices_sample.csv") as f:
        for line in f:
                if line[-1] == '\n':
                        line = line[:-1]
                (key, val) = line.split(',')
                x = datetime.datetime.fromtimestamp(int(key)).strftime('%Y-%m-%d -')
                weekday = datetime.datetime.fromtimestamp(int(key)).strftime('%w')
                (day, dash) = (str(x)).split(' ')
                if day in prices:
                        prices[day].append(val)
                else:
                        prices[day] = [val]
                firstdayofweek = (datetime.datetime.fromtimestamp(int(key)) - datetime.timedelta((int(weekday) - 1))).strftime('%Y-%m-%d')
                if firstdayofweek in weeks:
                        weeks[firstdayofweek].append(int(val))
                else:
                        weeks[firstdayofweek] = [int(val)]

print("File read, calculating values...")
for week, prices_of_week in weeks.items():
    min = 5000
    max = 0
    sum = 0
    counter = 0
    for price in prices_of_week:
        if price < min:
            min = price
        if price > max:
            max = price
        sum += price
        counter += 1
    minmaxave[week] = []
    minmaxave[week].append(min)
    minmaxave[week].append(max)
    minmaxave[week].append(sum/counter)
print("Writing to file...")
w = open("q2_result.csv", "w")
for week in minmaxave:
    w.write(week + "= Min: " + str(minmaxave[week][0]) + ", Max: " + str(minmaxave[week][1]) + ", Avg: " + str(minmaxave[week][2]) + '\n')
print("Writing complete.")
