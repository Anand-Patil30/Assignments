def sort_dictionary_by_key(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[0]))
    return sorted_dict


my_dict = {'Stark': 100, 'Thor': 97, 'Hulk': 95, 'Hawkey': 85 ,'Rogers':90}

modified_dict = sort_dictionary_by_key(my_dict)
print("Sorted Order : ", modified_dict)
