# def print_list(uncomplete_list,complete_list):
#     while uncomplete_list:
#         cur_val = uncomplete_list.pop()
#         print(cur_val)
#         complete_list.append(cur_val)
        


# def show_completed_list(complete_list,uncomplete_list):
#     print(len(uncomplete_list))
#     while complete_list:
#         cur_value = complete_list.pop()
#         print(cur_value)
        
        
# uncomplete_list = ['phone case', 'robot pendant',
# 'dodecahedron']
# complete_list = []


# # We can add slice to the function so we dont change the list but instead send a copy of it 
# print_list(uncomplete_list[:],complete_list)
# show_completed_list(complete_list,uncomplete_list)


def make_pizza(size, *toppings):
    print(f"{size},{toppings}")
    
