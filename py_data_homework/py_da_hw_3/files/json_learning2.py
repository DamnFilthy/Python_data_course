import json

purchase = open(r'C:\Users\User\Desktop\purchase_log.txt', 'r', encoding = 'UTF-8')
visit = open(r'C:\Users\User\Desktop\visit_log.csv', 'r', encoding = 'UTF-8')
funnel = open('funnel.csv', 'w')

next(purchase)
next(visit)

purchases = {}
for element, line in enumerate(purchase):
    line = line.strip()
    dict_ = json.loads(line)
    purchases.update({dict_['user_id'] : dict_['category'] })

for line in visit:
    line = line.strip()
    line = line.split(',')
    if line[0] in purchases.keys():
        funnel.write(line[0])
        funnel.write(' ')
        funnel.write(purchases[line[0]])
        funnel.write('\n')
