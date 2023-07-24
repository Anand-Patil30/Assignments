def String_Conv_Upper(string):
    upper_count = 0
    for char in string[:4]:
        if char.isupper():
            upper_count += 1
    if upper_count >= 2:
        print(string.upper())
    else:
        print(string)

string = input("Enter the string :")
String_Conv_Upper(string)
