#Задана натуральная степень k. Сформировать случайным образом 
#список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
#Пример:
#k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
#Функция формирующая список коэффициентов многочлена
def get_list_of_coef(number):
    list_of_coef = []
    for i in range(number):
        list_of_coef.append(random.randint(0, 100))
    return list_of_coef
#Функция формирует многочлен в виде строки
def get_polinomial_string(llist: list):
    polinomial = ""
    for i in range(len(llist)-1,-1, -1):
        if llist[i] == 0:
            continue
        #Если степень многочлена больше 1
        if i > 1:
            if llist[i] == 1:
                polinomial += f"X^{i+1} +"
            polinomial += f"{llist[i]}*X^{i+1} + "
        #Если степень многочлена равна 1
        elif i == 1:
            if llist[i] == 1:
                polinomial += f"X + "
            polinomial+= f"{llist[i]}*X + "
        #Если ноль
        else:
            polinomial+= f"{llist[i]} = 0" 
    return polinomial


if __name__ == "__main__":
    number = int(input("Задайте натуральную степень отличную от ноля и еденицы: "))
    if number == 1 or number == 0:
        print("Попробуйте ещё раз")
        exit()
    list_of_coef = get_list_of_coef(number)
    polinomial = get_polinomial_string(list_of_coef)
    file_name = "file_for_task.txt"
    #Делаем запись строки в файл
    with open(file_name, "w") as f:
        f.write(polinomial)
    print(f"Был создан файл: {file_name}")
    print(f"С многочленом: {polinomial}")