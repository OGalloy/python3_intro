#Задайте натуральное число N. Напишите программу, 
#которая составит список простых множителей числа N.

def get_simple_numbers(number: int) -> list :
    list_of_numbers = []
    divider = 2
    while (number // divider != 1):
        if number % divider == 0:
            number //= divider
            list_of_numbers.append(divider)
            continue
        divider += 1
    list_of_numbers.append(number)
    return list_of_numbers

print(get_simple_numbers(105000))    