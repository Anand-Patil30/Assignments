def match(dict1, dict2):
    for key in dict1:
        if key in dict2 and dict1[key] == dict2[key]:
            print(key + ": " + str(dict1[key]) + " is present in both x and y")
            
dict1 = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
dict2 = {'a': 1100, 'b': 2100, 'c': 1300, 'd': 4100, 'e': 500}

match(dict1, dict2)
