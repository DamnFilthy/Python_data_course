stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}

# Не хитрый подсчет
random_value, maximum_value = 0, 0
for v in stats.values():
  random_value = v
  if random_value > maximum_value:
    maximum_value = random_value

# Лайфхак
print(f'Максимальный объем продаж на рекламном канале: {list(stats.keys())[list(stats.values()).index(maximum_value)]}')
