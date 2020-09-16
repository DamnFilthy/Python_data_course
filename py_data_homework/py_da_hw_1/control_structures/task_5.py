a = ['2018-01-01', 'yandex', 'cpc', 100]
my_list = ['a', 'b', 'c', 'd', 'e', 'f']


c = {a[-2] : a[-1]}
for i in range(-3, -len(a) -1, -1):
  c = {a[i] : c}
print(c)

b = {my_list[-2] : my_list[-1]}
for i in range(-3, -len(my_list) -1, -1):
  b = {my_list[i] : b}
print(b)
