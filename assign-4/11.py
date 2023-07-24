def reverseString(string):
    reverse_string = string[ ::-1]
    if len(string) % 4 == 0:
        print(reverse_string)
    else:
        print(string)
string = input("Enter the string:")
reverseString(string)



