#Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def get_sum_odd_elements(int_elements: list):
    #возвращаем 0, если длина списка равна 0 или 1
    if len(int_elements) < 2:
        return 0
    # Вычисляем сумму нечётных элементов, итерируем список с шагом 2,
    # начиная с индекса 1.
    sum = 0
    for i in range(1, len(int_elements), 2):
        sum += int_elements[i]
        print(sum)
    return sum

if __name__ == '__main__':
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] #индексация с нуля.
    result = get_sum_odd_elements(elements)
    print(f"Сумма нечётных элементов списка {elements} равна: {result}")
    

