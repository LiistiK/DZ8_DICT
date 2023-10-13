pets = dict()
info = dict()
name_pet = input('Имя питомца: ')
pets[name_pet] = info
tip_pet = 'Вид питомца'
age_pet = 'Возраст питомца'
owner = 'Имя владельца'
info[tip_pet] = input('Вид питомца: ')
info[age_pet] = int(input('Возраст питомца: '))
info[owner] = input('Имя владельца: ')

if info[age_pet] % 10 in [1, 2, 3, 4]:
  print(f'Это {info[tip_pet]} по кличке "{name_pet}". Возраст питомца: {info[age_pet]} года. Имя владельца: {info[owner]}')
else:
  print(f'Это {info[tip_pet]} по кличке "{name_pet}". Возраст питомца: {info[age_pet]} лет. Имя владельца: {info[owner]}')

