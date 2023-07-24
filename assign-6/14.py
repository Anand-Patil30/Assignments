def is_dict_empty(dictionary):
    if dictionary:
        return False
    else:
        return True

my_dict = {}
if is_dict_empty(my_dict):
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.")
