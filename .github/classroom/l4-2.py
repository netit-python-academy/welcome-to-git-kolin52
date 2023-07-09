# Напишете програма, която показва знака (+ или -) от частното на две реални числа,
#без да го пресмята.
a = int(input('Write number: '))
b = int(input('Write number: '))
if a > 0 and b < 0 or a < 0 and b > 0:
    print('-')
elif a > 0 and b > 0 or a < 0 and b < 0:
    print('+')
else:
    print('Error')