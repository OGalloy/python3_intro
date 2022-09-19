#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. 
#Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
#За один ход можно забрать не более чем 28 конфет. 
#Все конфеты оппонента достаются сделавшему последний ход. 
#Сколько конфет нужно взять первому игроку, 
#чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""
from random import randint as r
candies = 2021
amount = 28
#Класс описывающий атрибуты и метод игрока
class Player:
    def __init__(self, name, turn):
        self.name = name
        self.turn = turn
    def move(self, taken_candies):
        global candies
        candies -= taken_candies
#Класс описывающий Бота
class Bot(Player):
    def move_bot(self):
        """Описываем поведение бота при игре"""
        global candies
        global amount
        print("Сейчас Бот берёт конфеты!!!")
        taken_candies = candies % amount
        if candies % amount == 0:
            return 1
        else:
            return candies % amount





if __name__ == '__main__':
    move = []
    taken_candies = 0
    type_of_game = input("Хотите сыграть с ботом? Напечатай \"bot\"? чтобы сыграть против машины!!!")
    if type_of_game == "bot":
        if r(0, 1) == 0:
            player1 = Bot("simpleBot", 0)
            player2 = Player("Human", 1)
            move = player1
        else: 
            player1 = Bot("simpleBot", 1)
            player2 = Player("Human", 0)
            move = player2
    else:
        if r(0, 1) == 0:
            player1 = Player("Human1", 0)
            player2 = Player("Human2", 1)
            move = player1
        else: 
            player1 = Bot("Human1", 1)
            player2 = Player("Human2", 0)
            move = player2
    print(player1.name, player1.turn)
    print(player2.name, player2.turn)

    #Основной цикл игры
    while (candies > 0):
        taken_candies = 0
        print(f"Конфет осталось: {candies}")
        if move.name == "simpleBot":
            taken_candies = move.move_bot()
        else:
            taken_candies = int(input(f"{move.name}!!Возьмите конфеты, но неболее 28: "))
        if taken_candies > amount or taken_candies <= 0:
            print("Неверное колличество конфет")
            continue
        #Методом move берём конфеты из кучи
        move.move(taken_candies)
        #Передаём ход другому игроку
        if move.turn == player1.turn:
            move = player2
        else:
            move = player1
        #Проверка на окончение игры
        if candies <= 28:
            print(f"{move.name}, Победил")
            break