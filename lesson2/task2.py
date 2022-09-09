#Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.
def get_amount(n):
    summary = 0
    for i in range(1, n + 1):
        summary +=i
    return summary

if __name__ == '__main__':
    print(get_amount(5))