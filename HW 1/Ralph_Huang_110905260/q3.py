#Your model should work well in theory, but it has a problem:
#Too many people know what you know, and you can’t profit using
#this strategy. You need to step up your game. What if you were
#able throw in more data to your model?
#Question. Write a program to parse and get all the
#Symbol, Last Price, Market Time, and Change fields
#from the "commodities futures" table from
#https://finance.yahoo.com/commodities. The program returns
#the a list of lists, where each list contains the
#Symbol, Name, Last Price and Market Time of a commodity.
#Write all these to a file named commodities.txt,
#one line for each commodity, and with comma separated values
#(e.g.,symbol, last price, market time, change )[15 pts].
#Hint: You do not have to use BeautifulSoup for this, but it
#may make things much easier

from bs4 import BeautifulSoup
import urllib.request

website = urllib.request.urlopen('https://finance.yahoo.com/commodities')

html_soup = BeautifulSoup(website, "html.parser")
type(html_soup)

table = html_soup.find(lambda tag: tag.name =='table' and tag.has_attr('data-reactid') and tag['data-reactid'] == "15")
rows = table.findAll(lambda tag: tag.name =='tr' and tag.has_attr('data-reactid') and int(tag['data-reactid']) > 45)

data = []
for row in rows:
    cols = row.findAll('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

w = open("commodities.txt", "w")
for i in range(len(data)):
        w.write(str(data[i][0]) + ", " + str(data[i][1]) + ", " + str(data[i][2]) + ", " + str(data[i][3]) + ", " + data[i][4] + "\n")
