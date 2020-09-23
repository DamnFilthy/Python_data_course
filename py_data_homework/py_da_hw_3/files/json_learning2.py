import json

purchases = []
i = 0
f = open('visit_log.csv', 'r')
d = open('funnel.csv', 'w')
for  line in f:
    line.strip().split(',')
    if line[1] != None:
        purchases = line.strip().split(',')
        d.write(str(purchases))
        d.write('\n')

d.close()
