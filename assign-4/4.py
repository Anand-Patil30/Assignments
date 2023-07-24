def replace_character(string):
    first_char = string[0] 
    updated_string = first_char
    
    for char in string[1:]:
        if char == first_char:
            updated_string += '$'
        else:
            updated_string += char
    return updated_string

string = input("Enter The String Sample")
result = replace_character(string)
print(result)
