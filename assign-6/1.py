def sort_dictionary_by_value(dictionary, reverse=False):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=reverse))
    return sorted_dict


my_dict = {'Stark': 100, 'Thor': 97, 'Hulk': 95, 'Hawkey': 85 ,'Rogers':90}

ascending_dict = sort_dictionary_by_value(my_dict)
print("Ascending order:", ascending_dict)


descending_dict = sort_dictionary_by_value(my_dict, reverse=True)
print("Descending order:", descending_dict)
