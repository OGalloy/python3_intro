my_list = [1,3,4,5,6,7]

print([i+1 for i in range(len(my_list)) if my_list[i]-1 != my_list[i-1]])