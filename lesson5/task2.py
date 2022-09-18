#Создайте программу для игры в ""Крестики-нолики"".
#Игровое поле
desk = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    def move(self, x, y ):
        desk[x][y] = self.symbol 


def print_desk():
    for i in range(len(desk)):
        for j in range(len(desk[0])):
            print(desk[i][j],  end = " ")
        print()

def check_desk(desk: list):
    #Проверка горизонталей
    for value in desk:
        if value == ["X", "X", "X"]:
            return [True, player1.name]
        elif value == ["O", "O", "O"]:
            return [True, player2.name]
    #Проверка вертикалей
    for i in range(len(desk[0])):
        if desk[0][i]== "X" and desk[1][i] == "X" and desk[2][i] == "X":
            return [True, player1.name]
        elif desk[0][i]== "O" and desk[1][i] == "O" and desk[2][i] == "O":
            return [True, player2.name]
    #Проверка главной диагонали.        
    if [desk[x][x] for x in range(len(desk))] == ["X", "X", "X"]:
        return [True, player1.name]
    elif [desk[x][x] for x in range(len(desk))] == ["O", "O", "O"]:
        return [True, player2.name]
    if [desk[x][-x-1] for x in range(len(desk))] == ["X", "X", "X"]:
        return [True, player1.name]
    elif [desk[x][-x-1] for x in range(len(desk))] == ["O", "O", "O"]:
        return [True, player2.name]
    return [False, "Ничья"]
    
        

if __name__ == '__main__':
    print("Привет, Давай сыграем в крестики-нолики!!!")
    player1_name = input("Введите имя первого игрока!!!")
    player2_name = input("Введите имя второго игрока!!!")
    print("Чтобы сделать ход введи номер строки и номер столбца!!!")
    player1 = Player(player1_name, "X")
    player2 = Player(player2_name, "O")
    game_over = [False, "Ничья"]
    round = 0
    while(game_over[0] != True ):
        print_desk()
        if round == 8:
            break
        if round % 2 == 0:
            moving =[int(x) for x in input(f"{player1.name} ваш ход!!!").split(" ")]
            if desk[moving[0]-1][moving[1]-1] == "*":
                player1.move(moving[0]-1, moving[1]-1)
                round +=1
        else:
            moving =[int(x) for x in input(f"{player2.name} ваш ход!!!").split(" ")]
            if desk[moving[0]-1][moving[1]-1] == "*":
                player2.move(moving[0]-1, moving[1]-1)
                round +=1
        game_over = check_desk(desk)
    print(print_desk())
    if game_over[1] == "Ничья":
        print("Ничья")
    else:
        print(f"Победил {game_over[1]}")