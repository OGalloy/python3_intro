import commands
###
def main():
    print("Приложение - телефонная книга!!!")
    while True:
        print("для получения справки введите help")
        command = input("cmd: ")
        commands.parse_command(command)

###
###
if __name__ == '__main__':
    main()