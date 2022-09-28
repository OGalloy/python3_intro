#1.Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
#Input: 5 -> 1 3 3 3 4
#Output: 1 3 3 3 1


rating = input("Введите оценки: ").split(" ")
rating =[int(i) for i in rating]
rating = [min(rating) if i is max(rating) else i  for i in rating]

print(rating)
