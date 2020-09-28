import json

purchases = {}
f = open(r'C:\Users\User\Desktop\purchase_log.txt', 'r', encoding = 'UTF-8')
d = open('results.txt', 'w')
next(f)
for element, line in enumerate(f):
    line = line.strip()
    dict_ = json.loads(line)
    purchases.update({dict_['user_id'] : dict_['category'] })

d.write(str(purchases))
d.write('\n')
d.close()

print(purchases)
