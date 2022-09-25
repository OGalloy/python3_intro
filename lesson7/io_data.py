#
import database

##
def create_new_contact():
    new_contact =  input("Введите ФИО нового контакта разделяя пробелом").split(" ")
    if len(new_contact) != 3:
        return print(">>Проверьте правильность данных")
    new_contact += [input(">>Введите номер нового контакта: ")]
    print(new_contact)
    database.create_cell(new_contact[0], new_contact[1], new_contact[2], new_contact[3])

##
def read_contact():
    contact = input(">>Введите ФИО контакта разделяя пробелом: ").split(" ")
    if len(contact) != 3:
        return print(">>Проверьте правильность данных")
    print(database.read_number(contact[0], contact[1], contact[2]))

##
def read_all_contacts():
    for data in database.read_all():
        print(f"{data[0]} {data[1]} {data[2]} {data[3]}")

def import_all():
    file_name = input(">>Введите Имя файла для импорта контактов в базу данных: ")
    data = ""
    with open(file_name, "r") as file:
        for line in file:
            data = line.replace("\n", "").split(" ")
            database.create_cell(data[0], data[1], data[2], data[3])

#export всех контактов в файл
def export_all():
    file_name = input(">>Введите имя файла для экспорта контактов: ")
    with open(file_name, "a") as file:
        for data in database.read_all():
            file.write(f"{data[0]} {data[1]} {data[2]} {data[3]}\n")

##
def export_contact():
    contact = input(">>Введите ФИО контакта разделяя пробелом: ").split(" ")
    if len(contact) != 3:
        return print(">>Проверьте правильность данных")
    result = database.export_contact(contact[0], contact[1], contact[2])
    file_name = input(">>Введите имя файла для импорта: ")
    with open(file_name, "a") as file:
        file.write(f"{result[0]} {result[1]} {result[2]} {result[3]}\n")
