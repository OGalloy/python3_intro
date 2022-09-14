#35. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

#Импорт функций из task4.py
import task4 as t
#Успользую регулярные выражения
import re
#функция получает из строки список целых чисел
def polinomial_to_int_list(poli: str):
    list_of_numbers = poli.split(" + ")
    
    for value in range(len(list_of_numbers)):
        #re.findal исользуем для нахождения строки. которая содержит цифры
        # "^" указывает на начало строки
        list_of_numbers[value] = int(re.findall("^[0-9]+", str(list_of_numbers[value]))[0])
    return list_of_numbers
#Функция складывает элементы списка 
def add_lists(list1, list2):
    if len(list1) <= len(list2):
        for i in range(len(list1)):
            list2[i] = list1[i] + list2[i]
        return list2[::-1]
    else:
        for i in range(len(list2)):
            list1[i] = list1[i] + list2[i]
        return list1[::-1]

if __name__ == "__main__":
    first_polinomial = t.get_polinomial_string(t.get_list_of_coef(5))
    second_polinomial = t.get_polinomial_string(t.get_list_of_coef(5))
    #Читаем два файла с многочленами
    poli1 = ""
    poli2 = ""
    with open("file1.txt", "r") as f:
        poli1 = f.read()
    with open("file2.txt", "r") as f:
        poli2 = f.read()
    print(poli1)
    print(poli2)
    poli1 = polinomial_to_int_list(poli1)
    poli2 = polinomial_to_int_list(poli2)
    new_polinomial = t.get_polinomial_string((add_lists(poli1, poli2)))
    print(new_polinomial)
    with open("file3.txt", "w") as f:
        f.write(new_polinomial)

    