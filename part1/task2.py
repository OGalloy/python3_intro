#Напишите программу для. проверки истинности утверждения 
#¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def test():
	for i in range(8):
		#переводим i в двоичный вид, после в int. и поразрядно подставляем 
		value = int('{:0b}'.format(i))
		#и поразрядно подставляем в выражение для проверки 
		x = (value // 100)
		y = (value % 100) // 10
		z = (value % 10)
		result = not (x or y or z) == (not x and not y and not z)
		# Вывод на экран
		print(f'x:{x} y:{y} z:{z} ')
		print(f'not (x or y or z) == (not x and not y and not z) equal: {result}')

if __name__ == '__main__':
	test()