#Задайте последовательность чисел. Напишите программу, 
#которая выведет список неповторяющихся элементов исходной последовательности.


def get_int_sequence(sequence:list) -> list:
    new_list = []
    for value in sequence:
        try: #Проверяем что значение в списке целое число
            value = int(value)
        except ValueError as e:
            print(e) #Если не целое, пишем ошибку и продолжаем цикл
            continue
        else:                    # Если ошибки нет, проверяем вхождения value в new_list.
            if value in new_list:#Тем самым исключаем повторы.
                continue
        new_list.append(value)
    return new_list



if __name__ == "__main__":
    sequence_of_numbers = input("Введите последовательность чисел, используя пробел.")
    raw_list = sequence_of_numbers.split(" ")
    print(f"Последвательность без повторений равна: {get_int_sequence(raw_list)} ")
    