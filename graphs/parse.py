import csv
import string
a=[]
i=0
file = open("data.csv","rb")
open_offers=[]
cycles=[]
contracts=[]
escrows=[]
for line in file.xreadlines():
     l = [i.strip() for i in line.split(',')]
     cycles.append(l[0])
     open_offers.append(l[1])
     contracts.append(l[2])
     escrows.append(l[3])
#print cycles
f=[]
g=[]
h=[]
j=[]
for i in cycles[1:]:
    a=int(i)
    f.append(a)
print f
#print type(cycles[2])
for i in open_offers[1:]:
    a=int(i)
    g.append(a)
print g

for i in contracts[1:]:
    a=int(i)
    h.append(a)
print h

for i in escrows[1:]:
    a=int(i)
    j.append(a)
print j
