#Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
#Пример:
#45 -> 101101
#3 -> 11
#2 -> 10


#Функция возвращает двоичное число ввиде строки
def int_to_bin(int_number: int):
    if int_number == 0:
        return "0"
    if int_number == 1:
        return "1"
    bin_string = ""
    while (int_number // 2 != 0):
        bin_string +=  str(int_number % 2)
        int_number //= 2
    bin_string += "1"
    return bin_string[::-1] #делаем реверс строки и возвращаем значение

if __name__ == '__main__':
    int_list = [45, 3, 2]
    print(f"Преобразуем десятичные элементы списка {int_list} в двоичные. ")
    print([int_to_bin(x) for x in [45, 3, 2]])