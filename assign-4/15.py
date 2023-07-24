string = input("Enter the string:")
char_count = {}

for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

sorted_counts = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

repeated_chars = ""
for char, count in sorted_counts:
    if count > 1:
        repeated_chars += f"{char} {count}\n"
print(repeated_chars.rstrip(", "))
