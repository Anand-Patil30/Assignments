def remove_duplicates(dictionary):
    unique_dict = {}
    seen_values = set()

    for key, value in dictionary.items():
        if value not in seen_values:
            unique_dict[key] = value
            seen_values.add(value)

    return unique_dict

my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
result_dict = remove_duplicates(my_dict)

print("Original dictionary:", my_dict)
print("Dictionary without duplicates:", result_dict)
