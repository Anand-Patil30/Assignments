string = input("Enter the string;")
result = ''
prev_char = None

for char in string:
    if char != prev_char:
        result += char
        prev_char = char

print(result)
