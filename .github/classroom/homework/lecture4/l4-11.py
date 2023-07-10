# Задача 11. Да се напише програма, която да намира медианата из между три стойности.

list_num = [7,15,3]
slist_num = list_num.sort()
num_list = len(list_num)
if num_list % 2 == 0:
    med = (list_num[num_list//2 - 1] + list_num[num_list//2]) / 2
else:
    med = list_num[num_list// 2]
print('Median is: ', str(med))
