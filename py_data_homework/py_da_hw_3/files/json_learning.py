import json

purchases = {}
i = 0
f = open('purchase_log.txt', 'r', encoding = 'UTF-8')
d = open('results.txt', 'w')
for element, line in enumerate(f):
    line = line.strip()
    dict_ = json.loads(line)
    purchases = {dict_['user_id'] , dict_['category'] }
    d.write(str(purchases))
    d.write('\n')

d.close()
