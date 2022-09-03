#Напишите программу, которая по заданному номеру четверти, 
#показывает диапазон возможных координат точек 
#в этой четверти (x и y).


def get_range(number_quarter: int):
    if number_quarter == 1:
        return f'Диапазон возможных значений X(0, +inf) Y(0, +inf)'
    if number_quarter == 2:
        return f'Диапазон возможных значений X(0, -inf) Y(0, +inf)'
    if number_quarter == 3:
        return f'Диапазон возможных значений X(0, -inf) Y(0, -inf)'
    if number_quarter == 4:
        return f'Диапазон возможных значений X(0, +inf) Y(0, -inf)'

if __name__ == '__main__':
    number = int(input("Введите номер четверти в двухмерном пространстве: "))
    print(get_range(number))