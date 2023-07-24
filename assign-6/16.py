def three_highest_values(dictionary, n):
    sorted_values = sorted(dictionary.values(), reverse=True)
    highest_values = sorted_values[:n]
    return highest_values

my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
n = 3

highest_values = three_highest_values(my_dict, n)
print("The highest", n, "values in the dictionary are:", highest_values)
