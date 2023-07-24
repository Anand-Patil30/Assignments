my_dict = {'Stark': 100, 'Thor': 97, 'Hulk': 95, 'Hawkey': 85 ,'Rogers':90}
    
def check_key(dictionary, key):
    if key in dictionary:
        my_dict.pop(key)
        print("Key '{}'  removed Successfully !!".format(key))
        print(my_dict)
    else:
        print("Key '{}'  does not exist in the dictionary.".format(key))

key=input("enter the key you want to remove: ")
        
check_key(my_dict, key)
