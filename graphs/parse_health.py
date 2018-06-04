import pandas as pd
import numpy as np
import csv
df = pd.read_csv("./health.csv")

#print df[['day','open_issues','closed_issues']]
days = df.day.values
openissues = df.open_issues.values
closedissues = df.closed_issues.values

d = days[0::4].tolist()
oi = [int(sum(openissues[current: current+4])) for current in xrange(0, len(openissues), 4)]
ci = [int(sum(closedissues[current: current+4])) for current in xrange(0, len(closedissues), 4)]
d.insert(0,'days')
oi.insert(0,"open issues at the end of a day")
ci.insert(0,"closed issues at the end of a day")


print "number of days",
num_days =df["day"].iloc[-1]
print num_days
#x = np.zeros((z,z,z))

print "total entries",
entries= df.shape[0]
print entries

print "number of headers",
headers= df.shape[1]
print headers

myData = [d,oi,ci]

c = open('health_issues.csv', 'w')
#"w" indicates that you're writing strings to the file

with c:
    writer = csv.writer(c)
    writer.writerows(myData)

print("Writing complete")
