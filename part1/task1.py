#Напишите программу, которая принимает на вход цифру, 
#обозначающую день недели, и проверяет, 
#является ли этот день выходным.
#Пример: - 6 -> да
#        - 7 -> да
#        - 1 -> нет
def is_day_off(week_day: int):
    #Проверка на корректное число
    if week_day > 7 or week_day < 1  or type(week_day) != type(1):
        print("Вы ввели некорректное число")
        exit()
    #Проверка что число является выходным днём   
    if 7 > week_day > 5:
        return True
    return False

if __name__ == '__main__':  
    input_value = input("Введите цифру дня недели: ")
    if is_day_off(int(input_value)) == True:
        print('Этот день является выходным.')
    else:
        print('Этот день не является выходным.')
