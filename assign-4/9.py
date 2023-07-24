string = input("Enter the string : ")
index = int(input("Enter the index : "))
if 0 <= index < len(string):
    new_string = string[:index]+string[index+1:]
    print(new_string)
