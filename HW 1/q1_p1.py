import datetime

prices = {}
print("Opening file")
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

w = open("q1_p1_result.csv", "w")
print("File read and dictionary created.\nWriting to file...")
for day in prices:
        writestr = ", ".join(prices[day])
        w.write(day + ": " + writestr + "\n")
print("Writing completed. Check q1_p1_result.csv; It is located in the same directory as this file.")
