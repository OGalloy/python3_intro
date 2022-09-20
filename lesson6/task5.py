def print_operation_table(operation, num_rows = 9, num_columns = 9):
    for row in range(1, num_rows):
        for columns in range(1, num_columns):
            print(operation(row, columns), end = " ")
        print()


print_operation_table(lambda x, y: x*y, 9, 9)
print()
print_operation_table(lambda x, y: x**y, 9, 9)