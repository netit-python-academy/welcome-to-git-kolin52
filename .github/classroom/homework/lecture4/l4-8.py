num = int(input('Insert number between 0 and 999: '))
#Дефинираме четири списъка с думи: ONES съдържа думите за числата 0-9, TEENS съдържа думите за числата 10-19
#и TENS съдържа думите кратни на 10 и HUNDREDS съдържа думите за числата 100 до 900.

ONES = ["", "едно", "две", "три", "четири", "пет", "шест", "седем", "осем", "девет"]  
TEENS = [ "", "единадесет", "дванадесет", "тринадесет", "четиринадесет", "петнадесет", "шестнадесет", \
         "седемнадесет", "осемнадесет", "деветнадесет"]  
TENS = [ "", "десет", "двадесет", "тридесет", "четиридесет", "петдесет", "шестдесет", "седемдесет", "осемдесет", "деветдесет"]
HUNDREDS = [ "","сто", "двеста", "триста", "четиристотин", "петстотин", "шестстотин", "седемстотин", "осемстотин", "деветстотин"]

if num == 0:  
    print("нула")  
#elif num < 0:
    #print("минус ", abs(num))
elif num < 10:  
    print( ONES[num])  
elif num < 20:
    # get from list the number 
    print( TEENS[num - 10]) 
elif num < 100:  
    print(TENS[num // 10], " и ",ONES[ num % 10 if num % 10 != 0 else ""]) 
# Числата от 100 до 900 разделяме на три групи      
elif 100 <= num < 110 or 200 <= num < 210 or 300 <= num < 310 or 400 <= num < 410 or 500 <= num < 510 \
     or 600 <= num < 610 or 700 <= num < 710 or 800 <= num < 810 or 900 <= num < 910:
    if num % 100 != 0:
        print(HUNDREDS[num // 100] + " и " + ONES[((num % 10)%10)] )  
    else:
        print(HUNDREDS[num // 100])  
             
elif 110 <= num < 120 or 210 <= num < 220 or 310 <= num < 320 or 410 <= num < 420 or 510 <= num < 520 \
     or 610 <= num < 620 or 710 <= num < 720 or 810 <= num < 820 or 910 <= num < 920:
    if num % 100 != 0:
        print(HUNDREDS[num // 100] + " и " + TEENS[((num % 10)%10)] )
    else:
        print(HUNDREDS[num // 100])
    
elif 120 <= num <= 999:
    if num % 100 != 0:
        print(HUNDREDS[num // 100] + " " + TENS[(num % 100)//10], " и ", ONES[ num % 10])
    else:
        print(HUNDREDS[num // 100])

else:  
    print("номерът е извън обхвата")  


