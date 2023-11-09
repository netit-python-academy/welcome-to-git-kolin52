a1 = int(input('insert number: '))
a2 = int(input('insert number: '))
a3 = int(input('insert number: '))

if a2 < a1 < a3:
    print(a3, a1, a2)
elif a2 < a3 < a1:
    print(a1, a3, a2)
elif a3 < a1 < a2:
    print(a2, a1, a3)
elif a3 < a2 < a1:
    print(a1, a2, a3)
elif a1 < a2 < a3:
    print(a3, a2, a1)
else:
    print(a2, a3, a1)



# second solution

a1 = int(input('insert number: '))
a2 = int(input('insert number: '))
a3 = int(input('insert number: '))

x1 = min(a1, a2, a3)
x2 = max(a1, a2, a3)
x3 = (a1 + a2 + a3) - x1 - x2

print(x2, x3, x1)


        