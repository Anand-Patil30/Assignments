sample_dict = {'a': 10, 'b': 20, 'c': 30}

def check_key(dictionary, key):
    if key in dictionary:
        print("Key '{}' exists in the dictionary.".format(key))
    else:
        print("Key '{}' does not exist in the dictionary.".format(key))

key = input("Enter the key to check: ")

check_key(sample_dict, key)
