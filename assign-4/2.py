string = input("Enter the string: ")
freq = {}

for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

sorted_dict = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

print("Frequency of character in string:\n"+str(sorted_dict))