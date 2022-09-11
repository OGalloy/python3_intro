#Задайте число. Составьте список чисел Фибоначчи, 
#в том числе для отрицательных индексов.(Доп)
#Пример:
#для k = 8 список будет выглядеть так: 
#[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

###
def get_negofib(n):
    int_list = [1,0,1]
    last_number = int_list[1]
    actual_number = int_list[2]
    for i in range(2, n+1):
        temp_val = actual_number
        actual_number = last_number + actual_number
        last_number = temp_val
        int_list.append(actual_number)
        print(i)
        if i % 2 == 0:
            int_list.insert(0, -1*actual_number)
        else:
            int_list.insert(0, actual_number)
    return int_list
result = get_negofib(0)
print(result)
    