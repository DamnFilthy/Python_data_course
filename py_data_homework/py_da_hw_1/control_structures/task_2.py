queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

word_in_string = [len(words.split()) for words in queries]

total = {}

for step in word_in_string:
     total[step] = total.get(step, 0) + 1
total = {element: count for element, count in total.items() if count >= 0}


for word_count, distribution in total.items():
 print(f'Количество слов в запросе: {word_count} - {distribution*100/len(queries)} %')
