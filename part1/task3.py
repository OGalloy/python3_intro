#Напишите программу, которая принимает на вход координаты точки (X и Y), 
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
#в которой находится эта точка (или на какой оси она находится).
#Пример:
#x=34; y=-30 -> 4
#x=2; y=4-> 1
#x=-34; y=-30 -> 3


def get_coordinate_quarter(x: int, y: int):
    if x == 0 or y == 0:
        print("Укажите координаты отличные от нуля")
        exit()
    if x > 0 and y > 0: 
        return 1
    if x > 0 and y < 0:
        return 4
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3

if __name__ == '__main__':
    x_coordinate = int(input("Введите координату X: "))
    y_coordinate = int(input("Введите координату Y: "))
    result = get_coordinate_quarter(x_coordinate, y_coordinate)
    print(f'Точка с координатами X: {x_coordinate}, Y: {y_coordinate}'
        + f' находится в квадрате под номером {result}')
