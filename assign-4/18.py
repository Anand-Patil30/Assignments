string = input("Enter the string : ")
modified_string = ""
for char in range(len(string)):
    if string[char] == ',':
        modified_string += '.'
    elif string[char] == '.':
        modified_string += ','
    else:
        modified_string += string[char]
print(modified_string)
