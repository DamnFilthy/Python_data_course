# Globular constants
FOUND_NAME = 1
SHELF_NUMBER = 2
SHOW_LIST_INFO = 3
ADD_DOCUMENT = 4
QUIT = 5

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
  }

# Main function
def main():
    choice = 0
    while choice != QUIT:
      choice = get_menu_choice()
      if choice == FOUND_NAME:
          found_name()
      elif choice == SHELF_NUMBER:
          shelf_number()
      elif choice == SHOW_LIST_INFO:
          show_list_info()
      elif choice == ADD_DOCUMENT:
          add_document()
    print('Программа завершила свою работу. До свидания.')

# Menu
def get_menu_choice():
  print('\n')
  print('Menu')
  print('-----------------------------')
  print('1. Найти имя по номеру документа.')
  print('2. Найти номер полки по номеру документа.')
  print('3. Вывести всю информацию, по всем документам')
  print('4. Добавить новый документ.')
  print('5. Выход')
  print('')

  # Get user answer
  choice = int(input('Enter the selected item: '))
  while choice < FOUND_NAME or choice > QUIT :
      choice = int(input('Enter the selected item: '))
  return choice

# Finds name by document number
def found_name():
  doc_num = input('Введите номер документа: ')
  for id, v in enumerate(documents):
    if doc_num == documents[id]["number"] :
      print(documents[id]["name"])
      break
    elif id == (len(documents) - 1):
      print('Документ не найден')
      break

# Finds the shelf on which the document is stored
def shelf_number():
  doc_num = input('Введите номер документа: ')
  count = 0
  for n,v in directories.items():
    count += 1
    if doc_num in v:
      print('Документ находится на полке №', n)
      break
    elif count == len(directories):
      print('Документ не найден.')

# Show all info
def show_list_info():
  for id, v in enumerate(documents):
    print('\n')
    for i in documents[id].values():
        print(i, end = ' ')

# Add document and shelf
def add_document():
  new_user = {}
  doc_type = input('Введите тип документа: ')
  doc_number = input('Введите номер документа: ')
  name = input('Введите ФИО владельца: ')

  new_user["type"] = doc_type
  new_user["number"] = doc_number
  new_user["name"] = name

  documents.append(new_user)
  print('Информация добавлена в базу.\n')

  shelf_number = input('Введите номер полки на которой будет хранится документ(1, 2, 3): ')
  try:
      directories[shelf_number].append(doc_number)
      print(f'Документ доставлен на полку №{shelf_number}.')
  except KeyError:
      print('Такой полки не существует. \n')
      directories[shelf_number] = [doc_number]
      print('Ваша полка была создана.')

main()
