def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None
    else:
        return(sorted(my_list)[1])

print(find_second_smallest([5, 8, 3, 2, 6]))
