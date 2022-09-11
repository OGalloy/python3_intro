#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]

def mul_pairs(actual_list: list) -> list:
    result_list = list()
    for i in range(len(actual_list) // 2):
        result_list.append(actual_list[i]*actual_list[-i-1])
    return result_list

if __name__ == '__main__':
    elements = [2, 3, 4, 5, 6, 2]
    result = mul_pairs(elements)
    print(f"Произведение пар элементов списка {elements} равно: {result}")
