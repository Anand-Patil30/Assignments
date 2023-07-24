def first_and_last_two_chars(string):
    if len(string) < 2:
        return ""  
    else:
        return string[:2] + string[-2:]

string = input("Enter The Sample String : ")
print(first_and_last_two_chars(string))  

