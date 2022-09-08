#На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
#а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, 
#чтобы все монетки были повернуты вверх одной и той же стороной.

#Единицы соответсвуют орлам, нули решкам
def get_minimal_value_coins(local_coins: list):
	#счётчик орлов
	count_heads = 0
	#счётчик решек
	count_tails = 0
	for i in range(len(local_coins)):
		if local_coins[i] == 1:
			count_heads+=1
		else:
			count_tails+=1	
	if count_heads == count_tails:
		return 0
	if count_heads < count_tails:
		return count_heads
	return count_tails

if __name__ == '__main__':
	#
	coins = [1, 0, 1, 1, 0, 0]
	print(get_minimal_value_coins(coins))
