#Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
def get_divider(n):
    for i in range(2, n+1):
        if not n % i:
            return i
if __name__ == '__main__':
    print(get_divider(25))