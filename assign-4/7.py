string = input("Enter the first string:")
first_index = string.find('not')
second_index = string.find('poor')

if first_index != -1 and second_index != -1 and first_index < second_index:
    substring_to_replace = string[first_index:(second_index+4)]
    replaced_string = string.replace(substring_to_replace, 'good')
    print(replaced_string)
else:
    print(string)
