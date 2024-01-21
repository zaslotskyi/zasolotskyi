#1
my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
second_list = []
zero = my_list.count(0)
for index in range(len(my_list)):
    if my_list[index] != 0:
        second_list.append(my_list[index])
second_list.extend([0] * zero)
print(second_list)








#2
my_list = [0, 1, 7, 2, 4, 8]
second_list = []
if len(my_list) == 0:
    print(0)
else:
    for i in range(len(my_list)):
        if i % 2 == 0:
            second_list.append(my_list[i])
    result = sum(second_list) * my_list[-1]
    print(result)

















