string = input("Enter the string: ")
if len(string)>=3:
    if string.endswith('ing'):
        string += 'ly'
        print(string)
    else:
        string += 'ing'
        print(string)
else:
    print(string)
