# Задача 4. Напишете програма, която за дадена цифра (0-5), зададена като вход, извежда името
# на цифрата на български език.

numb = int(input('Write number between 0 and 5: '))
if numb == 0:
    print('Нула')
elif numb == 1:
    print('Едно')
elif numb == 2:
    print('Две')
elif numb == 3:
    print('Три')
elif numb == 4:
    print('Четири')
else: 
    print('Пет')    

    