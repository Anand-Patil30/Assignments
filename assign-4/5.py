string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if len(string1) > 2 and len(string2) > 2:
    a = string2[:2]+string1[2:]
    b = string1[:2]+string2[2:]
    result = a+' '+b
    print(result)

else:
    print("Less character")
