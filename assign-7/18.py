def valid(s): return all([
    any(i.isupper() for i in s),      
    any(i.islower() for i in s),      
    any(i.isdigit() for i in s),      
    len(s) >= 10                     
])

input_string = input("Enter a string: ")

if valid(input_string):
    print("valid string")
else:
    print(" invalid string")
