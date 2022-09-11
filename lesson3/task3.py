#Задайте список из вещественных чисел. Напишите программу, 
#которая найдёт разницу между максимальным и минимальным значением 
#дробной части элементов.
#Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def sub_fractional_part(actual_list: list)->float:
    max_value = None
    min_value = None
    if actual_list[0] % 1 > actual_list[1] % 1:
        max_value = actual_list[0] % 1
        min_value = actual_list[1] % 1
    else:
        max_value = actual_list[1] % 1
        min_value = actual_list[0] % 1
    for i in range(2,len(actual_list)):
        if actual_list[i] % 1 > max_value:
            max_value = actual_list[i] % 1
            continue #Используем continue.так как далнейшее проверка условия бессмысленно
        if actual_list[i] % 1 < min_value:
            min_value = actual_list[i] % 1    
    return max_value - min_value

if __name__ in '__main__':
    list_float_values = [1.18, 1.18, 3.1, 5, 10.02]
    result = sub_fractional_part(list_float_values)
    print(f"Дано {list_float_values}")
    print(f"Разницу между максимальным и минимальным значением\
        дробной части элементов равна: {result}")