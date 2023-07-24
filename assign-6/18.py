def dictionaries_empty(dictionary_list):
    for dictionary in dictionary_list:
        if bool(dictionary): 
            return False
    return True

sample_list1 = [{}, {}, {}]
sample_list2 = [{1, 2}, {}, {}]

print(dictionaries_empty(sample_list1))  
print(dictionaries_empty(sample_list2)) 
