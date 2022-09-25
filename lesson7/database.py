###Модуль для работы с базой данных


import sqlite3
#Создаём соединение к базе данных, если такого файла нет, то файл создаётся.
con = sqlite3.connect('phonebook.db')

cur = con.cursor()
try:#Создаём таблицу с 4-мя столбцами
    cur.execute("CREATE TABLE phonebook(surname, name, patronymic, phone_number)")
except sqlite3.OperationalError:
    pass

#Создать новую ячейку в таблице с ФИО и номером телефона
def create_cell(surname: str, name: str, patronymic: str,  phone_number: str):
    cur.execute(f"INSERT INTO phonebook VALUES ('{surname}', '{name}', '{patronymic}', '{phone_number}')")
    return con.commit()

#Прочитать ячейку из таблицы по фио
def read_number(surname, name, patronymic):
    res = cur.execute(f"SELECT phone_number FROM phonebook WHERE surname='{surname}' AND name='{name}' AND patronymic='{patronymic}' ")
    return res.fetchone()

#Прочитать всю телефонную книгу
def read_all():
    res = cur.execute(f"SELECT * FROM phonebook")
    return res.fetchall()

#Обновить контакт
def update_number():
    pass

#Удаление из таблицы
def delete_cell(surname, name, patronymic):
    res = cur.execute(f"DELETE from phonebook WHERE surname='{surname}' AND name='{name}' AND patronymic='{patronymic}'")
    return res.commit()

#export контакта
def export_contact(surname: str, name: str, patronymic: str):
    res = cur.execute(f"SELECT surname, name, patronymic, phone_number FROM phonebook WHERE surname='{surname}' AND name='{name}' AND patronymic='{patronymic}'")
    return res.fetchone()
