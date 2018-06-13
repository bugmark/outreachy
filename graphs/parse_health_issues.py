import pandas as pd
import numpy as np
import csv
df = pd.read_csv("./health.csv")

#print df[['day','open_issues','closed_issues']]
days = df.day.values
openissues = df.issues_opened.values
closedissues = df.issues_closed.values

d = days[0::4].tolist()
oi = openissues[0::4].tolist()
ci = closedissues[0::4].tolist()
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

c = open('health_issues_noncumulative.csv', 'w')
#"w" indicates that you're writing strings to the file

with c:
    writer = csv.writer(c)
    writer.writerows(myData)

print("Writing complete")
