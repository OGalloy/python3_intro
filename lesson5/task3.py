#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

#Функция для кодировки 
def encode_rle(data:str):
    enc_string = ""
    count = 1
    char = data[0] 
    for i in range(1, len(data)):
        if data[i] == char:
            count += 1
        if data[i] != char or len(data) - 1 == i:
            enc_string += f"{count}{char}"
            char = data[i]
            count = 1
    return enc_string

# Функция для декодирования
def decode_rle(data:str):
    dec_string = ""
    number = data[0]
    for i in range(1, len(data)):
        try:#Пытаемся преобразовать символ строки к типу инт
            type(int(data[i])) == int

        except ValueError:#Если символ нельзя преобразовать к инт  
            dec_string += int(number) * data[i]
            number = ""
        else:#Если символ можно преобразовать в инт
            number += data[i]
            
    return dec_string

if __name__ == '__main__':
    print(encode_rle("aaaaccccbbbbb")) 
    print(decode_rle("14a4c5b"))

