import io_data as io
help_me = """
help - текушая справка, 
new - создание нового контакта,
read - чтение и вывод контакта по фио,
readall - чтение и вывод всей телефонной книги
export - экспорт одного контакта в файл
exportall - экспорт всех контактов в файл
import - импорт контактов из файла"""


def parse_command(cmd):
    if cmd == "help":
        print(help_me)
    elif cmd == "new":
        io.create_new_contact()
    elif cmd == "read":
        io.read_contact()
    elif cmd == "readall":
        io.read_all_contacts()
    elif cmd == "import":
        io.import_all()
    elif cmd == "export":
        io.export_contact()
    elif cmd == "exportall":
        io.export_all()
    else:
        print("Неизвестная команда.") 
