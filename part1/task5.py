#Напишите программу, которая принимает на вход координаты двух точек и #находит расстояние между ними в 2D пространстве.
#Пример:
#A(3,6); B(2,1) -> 5,09
#A(7,-5); B(1,-1) -> 7,21
import math

class Point:
    def __init__(self, x: int, y: int):
        """Конструктор"""
        self.x = x
        self.y = y

    def get_distance(self, other_point):
        """Метод для нахождения растояния между точками в 2D пространстве"""    
        return math.pow(((self.x - other_point.x)** 2 + (self.y - other_point.y)**2), 0.5)

if __name__ == '__main__':
    #Создаём два объекта Point
    first_point = Point(4, 4)
    second_point = Point(2, 2)
    print(f'Расстояние между точкой A({first_point.x}, {first_point.y})'+ 
          f' и B({second_point.x}, {second_point.y}) равно {first_point.get_distance(second_point)}')