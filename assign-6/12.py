def get_max_min(dictionary):
    values = list(dictionary.values())
    max_value = max(values)
    min_value = min(values)
    return max_value, min_value

my_dict = {'a': 10, 'b': 5, 'c': 15, 'd': 3}
max_val, min_val = get_max_min(my_dict)

print("Maximum value:", max_val)
print("Minimum value:", min_val)
