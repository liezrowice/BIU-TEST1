
#!/usr/bin/env python3



l1 = [315, 4, 66, 7, 2, 15, 3, 75, 4, 8, 4, 9]

max_num = l1[0]  

for num in l1:
    if num > max_num:
        max_num = num

print("The max number is:", max_num)



l1 = [315, 4, 66, 7, 2, 15, 3, 75, 4, 8, 4, 9]

max_num = l1[0]
the_second_max = float('-inf')  

for num in l1:
    if num > max_num:
        the_second_max = max_num  
        max_num = num
    elif num > the_second_max and num != max_num:
        the_second_max = num

print("The number in seconed place  is:", the_second_max)


