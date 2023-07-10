# Задача 10. Напишете програма, която да изчислява възрастта на дадено куче в кучешки
#години. Забележка: За първите две години, една кучешка година е равна на 10.5 човешки.
#След това всяка следваща кучешка година се равнява на 4-ри човешки години.

# formula for dog age - dog_age = a / 10.5 + b / 4

# Human life 

hum_age = float(input('Insert years: '))
if hum_age <= 21:
    dog_age = float(hum_age/10.5)
    print('Dog is ', dog_age, 'years old')
    
else:
    dog_age = float(hum_age - 21)/4 + 2
    print('Dog is ', dog_age, 'years old')

    